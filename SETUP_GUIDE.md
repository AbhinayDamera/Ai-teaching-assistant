# Quick Setup Guide - Voice-Enabled AI Teaching Assistant

## Step 1: Get Your Gemini API Key (Free!)

1. Go to: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the API key (starts with "AIza...")

## Step 2: Setup Environment

Open your terminal (PowerShell or CMD) in this folder and run:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows PowerShell)
venv\Scripts\Activate.ps1

# OR if using CMD
venv\Scripts\activate.bat
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**If PyAudio fails on Windows**, run this instead:
```bash
pip install pipwin
pipwin install pyaudio
pip install -r requirements.txt
```

## Step 4: Configure API Key

1. Create a file named `.env` in this folder
2. Add this line (replace with your actual key):
   ```
   GEMINI_API_KEY=AIza-your-actual-key-here
   ```

## Step 5: Run the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser at http://localhost:8501

## Troubleshooting

### "Python not found"
- Install Python from: https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

### "Microphone not working"
- Run the test: `python test_audio.py`
- Check browser permissions (click lock icon in address bar)
- Try Chrome browser (works best)

### "Module not found"
- Make sure virtual environment is activated
- Re-run: `pip install -r requirements.txt`

## Need Help?
- Check README.md for detailed documentation
- Check DEPLOYMENT.md for deployment options
