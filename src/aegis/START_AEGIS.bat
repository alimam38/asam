@echo off
echo ========================================
echo    AEGIS BACKEND - STARTING
echo ========================================
echo.

echo Navigating to aegis-backend folder...
cd /d "C:\Users\alima\Dropbox\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Aegis)\aegis-backend"

if errorlevel 1 (
    echo ERROR: Could not find aegis-backend folder
    echo.
    echo Please verify the folder exists at:
    echo C:\Users\alima\Dropbox\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Aegis)\aegis-backend
    echo.
    pause
    exit /b 1
)

echo Current directory: %CD%
echo.

echo Checking for requirements.txt...
if not exist requirements.txt (
    echo ERROR: requirements.txt not found in current directory
    echo.
    dir /b
    echo.
    pause
    exit /b 1
)

echo Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Installing requirements...
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo ERROR: Failed to install requirements
    pause
    exit /b 1
)

echo.
echo Checking for main.py...
if not exist main.py (
    echo ERROR: main.py not found in current directory
    echo.
    dir /b
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo    STARTING AEGIS SERVER
echo ========================================
echo.
echo Server will be available at:
echo http://localhost:8000
echo.
echo API Documentation at:
echo http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python main.py

pause
