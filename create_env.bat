@echo off
echo ============================================
echo Create .env Configuration File
echo ============================================
echo.

set /p API_KEY="Enter your Gemini API Key: "

echo Creating .env file...
(
echo # Google Gemini API Configuration
echo GEMINI_API_KEY=%API_KEY%
echo.
echo # Optional: Set to 'true' to enable debug mode
echo DEBUG_MODE=false
echo.
echo # Optional: Language preferences
echo DEFAULT_LANGUAGE=hinglish
echo SPEECH_RATE=150
) > .env

echo.
echo ============================================
echo .env file created successfully!
echo ============================================
echo.
echo You can now run: run.bat
echo.
pause
