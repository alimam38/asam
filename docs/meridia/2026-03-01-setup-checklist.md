# Meridia Command Center — Setup Checklist

**Time required:** 30 minutes at your desk. Everything below is sequential. Do it once and you're done.

---

## STEP 1: Create Your Dropbox Folders (2 minutes)

Open Dropbox. Create these folders if they don't exist:

```
Dropbox/Meridia/integra-core/
Dropbox/Turner/Financial Reports/
Dropbox/Turner/Student Accounts/
```

Move any existing Aegis backend code into `Dropbox/Meridia/integra-core/`. Move any Turner financial files into the appropriate Turner subfolder.

---

## STEP 2: Place the CLAUDE.md File (30 seconds)

Take the `CLAUDE.md` file from this package. Copy it into `Dropbox/Meridia/integra-core/`. This is the file Claude Code reads every time it opens that directory. It contains your architecture, endpoints, coding standards, and project structure.

---

## STEP 3: Set Up Cowork for Turner (3 minutes)

Open the Claude Desktop app. Click **Cowork**. It will ask you to select a folder. Navigate to `Dropbox/Turner/` and grant access.

Click the settings/instructions area (gear icon or "Set instructions"). Paste the contents of `COWORK_TURNER_INSTRUCTIONS.md` into the persistent instructions field. Save.

Cowork now knows your role, your standards, and your Turner context every time you open it.

---

## STEP 4: Set Up Claude Code for Meridia (3 minutes)

Open the Claude Desktop app. Click the **Code** tab. Navigate to `Dropbox/Meridia/integra-core/`. Claude Code will read the CLAUDE.md file and understand the entire project.

Type: "Read the CLAUDE.md and confirm you understand the Integra Core Services architecture."

It should respond with a summary of the endpoints, stack, and project structure. If it does, you're connected.

---

## STEP 5: Connect Google Drive (2 minutes)

In the Claude Desktop app, go to **Settings → Connectors**. Find Google Drive. Click Connect. Authorize with your Google account.

This lets Claude (in chat, Cowork, and Code) search and read your Drive files directly without you uploading anything.

---

## STEP 6: Verify Gmail Connection (1 minute)

In the same Connectors settings, confirm Gmail is connected. If not, connect it. This enables Cowork to draft, search, and organize emails — including sending student balance letters via mail merge if needed.

---

## STEP 7: Verify Canva Connection (1 minute)

Confirm Canva is connected in Connectors. This enables design creation for AME district work and Turner institutional materials directly from chat or Cowork.

---

## STEP 8: Install Claude in Chrome Extension (2 minutes)

Go to the Chrome Web Store. Search "Claude in Chrome" by Anthropic. Install it. Sign in with your Claude account.

This enables browser automation — navigating web portals, filling forms, extracting data from websites. Combined with Cowork, it creates a full automation loop.

---

## STEP 9: Test the Pipeline (5 minutes)

Open Cowork. Point it at `Dropbox/Turner/`. Drop any Turner financial file in the folder. Tell Cowork: "Review this file and identify any classification errors or posting issues."

If it reads the file, analyzes it, and gives you findings — the Turner pipeline is live.

Open Code. Navigate to `Dropbox/Meridia/integra-core/`. Tell Code: "Create the project structure defined in CLAUDE.md and build the FastAPI entry point with a health check endpoint."

If it creates files and writes code — the Meridia pipeline is live.

---

## STEP 10: Set a Recurring Task (2 minutes)

In Cowork, set up one recurring task to prove the concept. Example:

"Every Monday at 7 AM, check the Turner/Financial Reports folder for any new files. If there are new files, generate a summary of what was added and flag any concerns."

This runs in the background. You arrive at Turner on Monday to a briefing instead of a pile.

---

## DONE

You now have:

- **This chat** → Architecture, strategy, documents, design, complex analysis
- **Cowork** → Turner file operations, report generation, recurring automation
- **Code** → Meridia development, FastAPI backend, database work
- **Chrome** → Web automation, data extraction, portal navigation
- **Connectors** → Drive, Gmail, Calendar, Canva all feeding into every tool

Everything syncs through Dropbox. Every tool knows your standards. You work from anywhere — home, Turner, car, phone.

The command center is operational.
