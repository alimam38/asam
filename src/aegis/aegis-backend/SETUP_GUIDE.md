# 🚀 AEGIS BACKEND - COMPLETE SETUP GUIDE FOR BEGINNERS

**Welcome!** This guide will walk you through setting up the Aegis backend server step-by-step. No prior backend experience required.

---

## 📦 What You're Setting Up

You're about to run a **backend API server** that powers the Aegis Financial Positioning System. Think of it as the "engine" that provides data to the beautiful interface you see in `Index8.html`.

**What it does:**
- Provides financial position data (liquidity, net worth, etc.)
- Calculates Trust Index scores
- Runs "what if" scenario simulations
- Powers the Aletheia chat interface
- Manages governance alerts

---

## ✅ STEP 1: Check If You Have Python

Python is the programming language the server is written in.

### On Windows:
1. Press `Windows Key + R`
2. Type `cmd` and press Enter
3. In the black window, type: `python --version`
4. Press Enter

### On Mac:
1. Press `Command + Space`
2. Type `terminal` and press Enter
3. In the window, type: `python3 --version`
4. Press Enter

### What You Should See:
```
Python 3.11.x
```
or
```
Python 3.12.x
```

### ❌ If You Get an Error:
**You need to install Python.** Go to:
- Windows/Mac: https://www.python.org/downloads/
- Download Python 3.11 or newer
- During installation, **CHECK THE BOX** that says "Add Python to PATH"
- Restart your computer after installation

---

## 📁 STEP 2: Get the Backend Files

You need all these files in one folder:

```
aegis-backend/
├── main.py
├── api_v1.py
├── models.py
├── data_generator.py
├── requirements.txt
├── README.md
└── SETUP_GUIDE.md (this file)
```

### Option A: If You're Working in Claude
All files are already in `/home/claude/aegis-backend/` - you can download them or copy them.

### Option B: Manual Creation
1. Create a new folder called `aegis-backend` on your Desktop
2. Inside that folder, create 6 new text files with these exact names:
   - `main.py`
   - `api_v1.py`
   - `models.py`
   - `data_generator.py`
   - `requirements.txt`
   - `README.md`
3. Copy the code from each file into the corresponding `.py` file

---

## 🔧 STEP 3: Open a Terminal in Your Backend Folder

### On Windows:
1. Open File Explorer
2. Navigate to your `aegis-backend` folder
3. Click in the address bar at the top
4. Type `cmd` and press Enter
5. A black command window will open **in that folder**

### On Mac:
1. Open Finder
2. Navigate to your `aegis-backend` folder
3. Right-click the folder and select "New Terminal at Folder"
   (Or: Open Terminal, type `cd ` (with a space), then drag the folder into Terminal)

### Verify You're in the Right Place:
Type this command:
```bash
dir
```
(On Mac, use `ls` instead)

You should see your files listed:
```
main.py
api_v1.py
models.py
data_generator.py
requirements.txt
README.md
```

---

## 🐍 STEP 4: Create a Virtual Environment

A "virtual environment" is like a clean workspace for this project. It keeps the project's dependencies separate from your system.

### Type this command:

**On Windows:**
```bash
python -m venv venv
```

**On Mac/Linux:**
```bash
python3 -m venv venv
```

**What happens:** Python creates a new folder called `venv` inside your `aegis-backend` folder. This will take 10-30 seconds.

---

## 🔌 STEP 5: Activate the Virtual Environment

Now we "turn on" the virtual environment.

### On Windows:
```bash
venv\Scripts\activate
```

### On Mac/Linux:
```bash
source venv/bin/activate
```

### What You Should See:
Your command prompt will change to show `(venv)` at the beginning:

**Before:**
```
C:\Users\YourName\Desktop\aegis-backend>
```

**After:**
```
(venv) C:\Users\YourName\Desktop\aegis-backend>
```

✅ **If you see `(venv)`, you're ready to proceed!**

---

## 📥 STEP 6: Install Required Packages

Now we install the "dependencies" - the extra code libraries the server needs.

### Type this command:
```bash
pip install -r requirements.txt
```

### What happens:
You'll see text scrolling by as Python downloads and installs:
- FastAPI (the web framework)
- Uvicorn (the server)
- Pydantic (data validation)
- Faker (mock data generation)
- And a few others

**This will take 1-3 minutes.**

### What You Should See:
```
Successfully installed fastapi-0.104.1 uvicorn-0.24.0 pydantic-2.5.0 ...
```

### ❌ If You Get an Error:
- **"pip is not recognized"**: Your Python installation didn't add pip to PATH. Try `python -m pip install -r requirements.txt`
- **"No internet connection"**: You need internet to download packages
- **Permission error**: On Mac, try `pip install -r requirements.txt --user`

---

## 🎯 STEP 7: Start the Server!

You're ready! Let's start the Aegis backend.

### Type this command:
```bash
python main.py
```

### What You Should See:

```
================================================================================
AEGIS FINANCIAL POSITIONING SYSTEM
Ethical Steward • Dynamic Guidance System
================================================================================
✓ Server starting...
✓ API v1 loaded
✓ CORS configured
✓ Mock data generators ready

Documentation: http://localhost:8000/docs
Manifest: http://localhost:8000/manifest

Ready to receive requests.
================================================================================
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using WatchFiles
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

✅ **SUCCESS! Your server is running!**

---

## 🌐 STEP 8: Test Your Server

### Method 1: Browser Test (Easiest)
1. Open your web browser
2. Go to: `http://localhost:8000`
3. You should see a JSON response with Aegis information

### Method 2: Interactive Documentation
1. Go to: `http://localhost:8000/docs`
2. You'll see a beautiful interactive API documentation page
3. Click on any endpoint (like "GET /api/v1/position-grid")
4. Click "Try it out"
5. Click "Execute"
6. Scroll down to see the response!

### Method 3: Test a Specific Endpoint
Go to: `http://localhost:8000/api/v1/trust-index`

You should see JSON data like:
```json
{
  "overall_score": 87,
  "dimensions": [
    {"label": "Financial", "value": 90, "color": "var(--accent-emerald)"},
    ...
  ],
  "timestamp": "2024-01-20T10:00:00Z",
  ...
}
```

---

## 🎨 STEP 9: Connect to Your Frontend (Optional)

If you want to connect the `Index8.html` frontend to this backend:

### Quick Test:
1. Open `Index8.html` in a text editor
2. Find the JavaScript section (near the bottom)
3. Add this code to test the connection:

```javascript
// Add this right after the intro-enter click handler
fetch('http://localhost:8000/api/v1/position-grid')
  .then(response => response.json())
  .then(data => {
    console.log('Backend connection successful!', data);
  })
  .catch(error => {
    console.error('Backend connection failed:', error);
  });
```

4. Open `Index8.html` in your browser
5. Press `F12` to open Developer Tools
6. Click the "Console" tab
7. You should see: `Backend connection successful!` with data

### Full Integration:
See the "Integration with Frontend" section in `README.md` for complete instructions on replacing the mock data with live API calls.

---

## 🛑 STEP 10: Stop the Server

When you're done testing:

1. Go back to your terminal window
2. Press `Ctrl+C` (on both Windows and Mac)
3. The server will shut down gracefully

```
================================================================================
AEGIS SERVER SHUTTING DOWN
================================================================================
```

---

## 🔄 Running the Server Again Later

### Quick Start (After Initial Setup):

1. **Open terminal in the `aegis-backend` folder**

2. **Activate the virtual environment:**
   - Windows: `venv\Scripts\activate`
   - Mac: `source venv/bin/activate`

3. **Start the server:**
   ```bash
   python main.py
   ```

That's it! You don't need to reinstall packages.

---

## 🧪 Exploring the API

### Try These Endpoints in Your Browser:

**Basic Information:**
- http://localhost:8000 - Root endpoint
- http://localhost:8000/manifest - System manifest
- http://localhost:8000/api/v1/health - Health check

**Financial Data:**
- http://localhost:8000/api/v1/position-grid - Position metrics
- http://localhost:8000/api/v1/trust-index - Trust Index
- http://localhost:8000/api/v1/entities - All entities
- http://localhost:8000/api/v1/signal-feed - Signal feed
- http://localhost:8000/api/v1/metrics-dashboard - Metrics

**Interactive Docs:**
- http://localhost:8000/docs - Try all endpoints interactively!

---

## 🧰 Troubleshooting Common Issues

### "Port 8000 is already in use"
**Problem:** Another program is using port 8000.

**Solution 1 - Use a Different Port:**
In `main.py`, change the last line from:
```python
port=8000,
```
to:
```python
port=8001,
```
Then access the server at `http://localhost:8001`

**Solution 2 - Kill the Other Process:**
- Windows: Open Task Manager, find "Python", end the task
- Mac: Terminal: `lsof -ti:8000 | xargs kill -9`

### "Module not found" errors
**Problem:** Dependencies not installed correctly.

**Solution:**
1. Make sure virtual environment is activated (you see `(venv)`)
2. Run: `pip install -r requirements.txt` again
3. If still failing, try: `pip install fastapi uvicorn pydantic faker`

### "Python is not recognized"
**Problem:** Python not added to PATH during installation.

**Solution:**
1. Uninstall Python
2. Download from python.org again
3. **CHECK "Add Python to PATH"** during installation
4. Restart computer

### Virtual environment won't activate
**Problem:** Security policy on Windows.

**Solution:**
1. Open PowerShell as Administrator
2. Run: `Set-ExecutionPolicy RemoteSigned`
3. Type 'Y' and press Enter
4. Try activating again

### Can't install packages (403/404 errors)
**Problem:** Firewall/proxy blocking downloads.

**Solution:**
- Check your internet connection
- Temporarily disable VPN if using one
- Try on a different network

---

## 📚 Next Steps

Once your server is running:

1. **Explore the API Documentation**: http://localhost:8000/docs
2. **Test Each Endpoint**: Try fetching position data, trust index, etc.
3. **Run Scenarios**: Use the POST /scenario-engine endpoint
4. **Integrate with Frontend**: Connect Index8.html to the live backend
5. **Read the Architecture Doc**: Understand how to build out the full system

---

## 💡 Understanding What You've Built

### What is an API?
An **API** (Application Programming Interface) is like a menu at a restaurant:
- The menu lists what you can order (endpoints)
- You make a request (order food)
- The kitchen prepares it (server processes)
- You get your food (server sends data back)

### What is JSON?
**JSON** is how computers share structured data. Example:
```json
{
  "name": "Crown Legacy Trust",
  "value": "$12.4M",
  "status": "healthy"
}
```

### How Does This Connect to Index8.html?
- **Index8.html** = The beautiful interface (frontend)
- **This backend** = The engine providing data
- **Connection** = Frontend makes HTTP requests to backend
- **Result** = Live data instead of hardcoded values!

---

## 🆘 Still Stuck?

If you're having trouble:

1. **Check the error message carefully** - It usually tells you what's wrong
2. **Google the exact error** - Others have likely solved it
3. **Verify each step** - Go back through this guide slowly
4. **Check Python version** - Must be 3.11+
5. **Try a fresh start** - Delete the `venv` folder and start from Step 4

---

## 🎉 Success!

If you've made it here and your server is running - **congratulations!** 

You've just:
- Set up a Python virtual environment
- Installed backend dependencies
- Launched a FastAPI server
- Created a working API for the Aegis system

This is real backend development. You're now running production-quality code that could power an actual financial positioning system.

**Next:** Check out the Technical Architecture Document (Phase 2) to see how this prototype evolves into a full production system.

---

**Built with clarity. Governed by design. Stewarded with care.**

Need help? The error messages are your friends - they tell you exactly what's wrong.
