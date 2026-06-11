"""
Meridia Corpus Receiver — MCP Server
Receives conversations and project files from OpenAI Business Workspace
and stores them on the NAS for ingestion into the cognitive corpus.

Deploy as Docker container on Synology NAS.
Accessible at https://integra.meridiahq.com/mcp
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List
import json, os, time
from datetime import datetime

app = FastAPI(title="Meridia Corpus Receiver", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CORPUS_DIR = "/data/corpus/business_workspace"
os.makedirs(CORPUS_DIR, exist_ok=True)
os.makedirs(f"{CORPUS_DIR}/conversations", exist_ok=True)
os.makedirs(f"{CORPUS_DIR}/projects", exist_ok=True)
os.makedirs(f"{CORPUS_DIR}/raw", exist_ok=True)

# ── MCP Protocol Endpoints ──

@app.get("/mcp")
async def mcp_discovery():
    """MCP server discovery endpoint"""
    return {
        "name": "meridia-corpus-receiver",
        "version": "1.0.0",
        "description": "Receives and stores conversation content for Meridia corpus ingestion",
        "tools": [
            {
                "name": "store_conversation",
                "description": "Store a complete conversation with all messages. Use this to send an entire conversation thread to the Meridia corpus.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "Title of the conversation"
                        },
                        "project_name": {
                            "type": "string",
                            "description": "Name of the project this conversation belongs to, or 'none' if not in a project"
                        },
                        "messages": {
                            "type": "array",
                            "description": "Array of message objects with 'role' (user/assistant) and 'content' fields",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "role": {"type": "string"},
                                    "content": {"type": "string"}
                                }
                            }
                        },
                        "metadata": {
                            "type": "string",
                            "description": "Any additional context about this conversation"
                        }
                    },
                    "required": ["title", "messages"]
                }
            },
            {
                "name": "store_document",
                "description": "Store a document or file content. Use this to send project files, instructions, or any document to the Meridia corpus.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filename": {
                            "type": "string",
                            "description": "Name of the file"
                        },
                        "project_name": {
                            "type": "string",
                            "description": "Name of the project this file belongs to"
                        },
                        "content": {
                            "type": "string",
                            "description": "Full text content of the document"
                        },
                        "file_type": {
                            "type": "string",
                            "description": "Type of file (instruction, knowledge, conversation, code, etc.)"
                        }
                    },
                    "required": ["filename", "content"]
                }
            },
            {
                "name": "store_project_overview",
                "description": "Store an overview of a project including its name, description, instructions, and list of files. Use this before sending individual conversations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_name": {
                            "type": "string",
                            "description": "Name of the project"
                        },
                        "description": {
                            "type": "string",
                            "description": "Description of the project"
                        },
                        "instructions": {
                            "type": "string",
                            "description": "The project's system instructions or custom instructions"
                        },
                        "file_list": {
                            "type": "array",
                            "description": "List of files in the project",
                            "items": {"type": "string"}
                        },
                        "conversation_count": {
                            "type": "integer",
                            "description": "Number of conversations in this project"
                        }
                    },
                    "required": ["project_name"]
                }
            },
            {
                "name": "store_raw",
                "description": "Store any raw content that doesn't fit other categories. Use as a catch-all for any data that should be preserved.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "label": {
                            "type": "string",
                            "description": "A label for this content"
                        },
                        "content": {
                            "type": "string",
                            "description": "The content to store"
                        }
                    },
                    "required": ["label", "content"]
                }
            },
            {
                "name": "list_stored",
                "description": "List all content that has been stored so far. Use this to check what has already been sent.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        ]
    }


@app.post("/mcp/tools/{tool_name}")
async def execute_tool(tool_name: str, request: Request):
    """Execute an MCP tool"""
    body = await request.json()
    params = body.get("parameters", body)
    
    if tool_name == "store_conversation":
        return await store_conversation(params)
    elif tool_name == "store_document":
        return await store_document(params)
    elif tool_name == "store_project_overview":
        return await store_project_overview(params)
    elif tool_name == "store_raw":
        return await store_raw(params)
    elif tool_name == "list_stored":
        return await list_stored()
    else:
        return JSONResponse(status_code=404, content={"error": f"Unknown tool: {tool_name}"})


# Also handle direct POST for simpler MCP implementations
@app.post("/mcp")
async def mcp_execute(request: Request):
    """Handle MCP tool calls via POST to /mcp"""
    body = await request.json()
    
    # Handle different MCP request formats
    tool_name = body.get("tool", body.get("name", body.get("method", "")))
    params = body.get("parameters", body.get("params", body.get("arguments", body)))
    
    if tool_name == "store_conversation":
        return await store_conversation(params)
    elif tool_name == "store_document":
        return await store_document(params)
    elif tool_name == "store_project_overview":
        return await store_project_overview(params)
    elif tool_name == "store_raw":
        return await store_raw(params)
    elif tool_name == "list_stored":
        return await list_stored()
    else:
        # If no tool specified, try to store as raw
        return await store_raw({"label": f"unknown_{int(time.time())}", "content": json.dumps(body)})


async def store_conversation(params):
    title = params.get("title", "untitled")
    project = params.get("project_name", "none")
    messages = params.get("messages", [])
    metadata = params.get("metadata", "")
    
    safe_title = "".join(c if c.isalnum() or c in "-_ " else "" for c in title).strip().replace(" ", "_")[:80]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if project and project != "none":
        safe_project = "".join(c if c.isalnum() or c in "-_ " else "" for c in project).strip().replace(" ", "_")
        outdir = f"{CORPUS_DIR}/projects/{safe_project}"
        os.makedirs(outdir, exist_ok=True)
    else:
        outdir = f"{CORPUS_DIR}/conversations"
    
    data = {
        "title": title,
        "project": project,
        "message_count": len(messages),
        "messages": messages,
        "metadata": metadata,
        "received_at": datetime.now().isoformat(),
        "total_chars": sum(len(m.get("content", "")) for m in messages)
    }
    
    fpath = os.path.join(outdir, f"{timestamp}_{safe_title}.json")
    with open(fpath, "w") as f:
        json.dump(data, f, indent=2)
    
    return {
        "status": "stored",
        "title": title,
        "messages": len(messages),
        "chars": data["total_chars"],
        "path": fpath
    }


async def store_document(params):
    filename = params.get("filename", "untitled")
    project = params.get("project_name", "none")
    content = params.get("content", "")
    file_type = params.get("file_type", "unknown")
    
    safe_name = "".join(c if c.isalnum() or c in "-_. " else "" for c in filename).strip().replace(" ", "_")
    
    if project and project != "none":
        safe_project = "".join(c if c.isalnum() or c in "-_ " else "" for c in project).strip().replace(" ", "_")
        outdir = f"{CORPUS_DIR}/projects/{safe_project}/files"
        os.makedirs(outdir, exist_ok=True)
    else:
        outdir = f"{CORPUS_DIR}/raw"
    
    data = {
        "filename": filename,
        "project": project,
        "file_type": file_type,
        "content": content,
        "chars": len(content),
        "received_at": datetime.now().isoformat()
    }
    
    fpath = os.path.join(outdir, f"{safe_name}.json")
    with open(fpath, "w") as f:
        json.dump(data, f, indent=2)
    
    return {
        "status": "stored",
        "filename": filename,
        "chars": len(content),
        "path": fpath
    }


async def store_project_overview(params):
    project = params.get("project_name", "unknown")
    safe_project = "".join(c if c.isalnum() or c in "-_ " else "" for c in project).strip().replace(" ", "_")
    outdir = f"{CORPUS_DIR}/projects/{safe_project}"
    os.makedirs(outdir, exist_ok=True)
    
    data = {
        "project_name": project,
        "description": params.get("description", ""),
        "instructions": params.get("instructions", ""),
        "file_list": params.get("file_list", []),
        "conversation_count": params.get("conversation_count", 0),
        "received_at": datetime.now().isoformat()
    }
    
    fpath = os.path.join(outdir, "_overview.json")
    with open(fpath, "w") as f:
        json.dump(data, f, indent=2)
    
    return {
        "status": "stored",
        "project": project,
        "path": fpath
    }


async def store_raw(params):
    label = params.get("label", f"raw_{int(time.time())}")
    content = params.get("content", "")
    safe_label = "".join(c if c.isalnum() or c in "-_ " else "" for c in label).strip().replace(" ", "_")[:80]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    fpath = f"{CORPUS_DIR}/raw/{timestamp}_{safe_label}.json"
    with open(fpath, "w") as f:
        json.dump({"label": label, "content": content, "received_at": datetime.now().isoformat()}, f, indent=2)
    
    return {"status": "stored", "label": label, "chars": len(content), "path": fpath}


async def list_stored():
    result = {"projects": {}, "conversations": [], "raw": []}
    
    conv_dir = f"{CORPUS_DIR}/conversations"
    if os.path.isdir(conv_dir):
        result["conversations"] = sorted(os.listdir(conv_dir))
    
    proj_dir = f"{CORPUS_DIR}/projects"
    if os.path.isdir(proj_dir):
        for p in sorted(os.listdir(proj_dir)):
            ppath = os.path.join(proj_dir, p)
            if os.path.isdir(ppath):
                result["projects"][p] = sorted(os.listdir(ppath))
    
    raw_dir = f"{CORPUS_DIR}/raw"
    if os.path.isdir(raw_dir):
        result["raw"] = sorted(os.listdir(raw_dir))
    
    return result


@app.get("/mcp/health")
async def health():
    return {"status": "healthy", "stored": await list_stored()}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
