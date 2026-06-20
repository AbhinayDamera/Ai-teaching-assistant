@echo off
echo ============================================
echo Voice-Enabled AI Teaching Assistant Setup
echo ============================================
echo.

echo Step 1: Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)
echo Done!
echo.

echo Step 2: Activating virtual environment...
call venv\Scripts\activate.bat
echo Done!
echo.

echo Step 3: Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo WARNING: Some packages failed to install
    echo Trying to install PyAudio separately...
    pip install pipwin
    pipwin install pyaudio
    pip install -r requirements.txt
)
echo Done!
echo.

echo ============================================
echo Setup Complete!
echo ============================================
echo.
echo Next steps:
echo 1. Get your FREE Gemini API key from:
echo    https://makersuite.google.com/app/apikey
echo.
echo 2. Create a file named .env in this folder
echo.
echo 3. Add this line to .env file:
echo    GEMINI_API_KEY=your-api-key-here
echo.
echo 4. Run: run.bat
echo.
pause
