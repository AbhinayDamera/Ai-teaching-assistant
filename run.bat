@echo off
echo ============================================
echo Starting Voice-Enabled AI Teaching Assistant
echo ============================================
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Please run setup.bat first
    pause
    exit /b 1
)

REM Check if .env file exists
if not exist ".env" (
    echo WARNING: .env file not found!
    echo.
    echo Please create .env file with your Gemini API key:
    echo 1. Create a file named .env
    echo 2. Add: GEMINI_API_KEY=your-api-key-here
    echo.
    echo Get free API key from: https://makersuite.google.com/app/apikey
    echo.
    pause
    exit /b 1
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Starting application...
echo.
echo The app will open in your browser automatically.
echo Press Ctrl+C to stop the application.
echo.
streamlit run app.py

pause
