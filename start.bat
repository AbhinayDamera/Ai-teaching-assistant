@echo off
REM Quick Start Script for Voice Teaching Assistant (Windows)
REM Run this after initial setup

echo.
echo Starting Voice Teaching Assistant...
echo.

REM Check if backend/.env exists
if not exist "backend\.env" (
    echo Error: backend\.env file not found!
    echo Please create it from backend\.env.example and add your GEMINI_API_KEY
    pause
    exit /b 1
)

REM Start backend
echo Starting backend server...
cd backend
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo Error: Virtual environment not found. Run setup first:
    echo    cd backend
    echo    python -m venv venv
    echo    pip install -r requirements.txt
    pause
    exit /b 1
)
start "Backend Server" cmd /k python app.py
cd ..

REM Wait for backend to start
echo Waiting for backend to start...
timeout /t 5 /nobreak > nul

REM Start frontend
echo Starting frontend...
cd frontend

if not exist "node_modules" (
    echo Installing frontend dependencies...
    call npm install
)

start "Frontend Server" cmd /k npm start
cd ..

echo.
echo Application started!
echo.
echo Backend:  http://localhost:5000
echo Frontend: http://localhost:3000
echo.
echo Close the terminal windows to stop the servers
echo.
pause
