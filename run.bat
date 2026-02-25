@echo off
echo =========================================
echo  🍲 How Many Cals Bot Setup (Windows)
echo =========================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [Error] Python is not installed or not in your PATH.
    pause
    exit /b 1
)

REM Check if .env exists
if not exist ".env" (
    echo [Warning] .env file not found! Copying from .env.example...
    copy .env.example .env
    echo [Action] Please open the .env file and add your GEMINI and LINE API keys, then run this script again.
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist "venv\Scripts\activate.bat" (
    echo [Info] Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo [Info] Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo [Info] Installing requirements...
pip install -r requirements.txt --quiet

REM Run the app
echo 🚀 Starting FastAPI server with hot-reload...
python -m app.main

pause
