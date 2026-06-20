# 🚀 Setup Guide - Voice-Enabled AI Teaching Assistant

## Prerequisites

- **Python 3.9+** (for backend)
- **Node.js 16+** (for frontend)
- **Microphone** (for voice input)
- **Google Gemini API Key** (free from Google AI Studio)

## Step 1: Get Your Free Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the API key (starts with `AIza...`)

## Step 2: Backend Setup

```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Windows (CMD)
venv\Scripts\activate.bat
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### PyAudio Installation (Windows)

If PyAudio fails to install:
```bash
pip install pipwin
pipwin install pyaudio
```

### Configure API Key

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your Gemini API key
# GEMINI_API_KEY=your_actual_api_key_here
```

### Start Backend Server

```bash
python app.py
```

Backend will run on `http://localhost:5000`

## Step 3: Frontend Setup

Open a NEW terminal window:

```bash
# Navigate to frontend folder
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

Frontend will open automatically on `http://localhost:3000`

## Step 4: Test the Application

1. **Home Screen**: You should see two mode cards
2. **Click "Explain Concept"**:
   - Type a question OR hold the mic button and speak
   - Get AI explanation with voice output
3. **Click "Quiz Mode"**:
   - Enter a topic
   - Answer multiple-choice questions
   - See your score

## Troubleshooting

### Backend Issues

**"ModuleNotFoundError: No module named 'flask'"**
- Make sure virtual environment is activated
- Run `pip install -r requirements.txt` again

**"GEMINI_API_KEY not found"**
- Check `.env` file exists in `backend/` folder
- Verify API key is correctly pasted without quotes

**PyAudio installation fails**
- Windows: Use `pipwin install pyaudio`
- Mac: `brew install portaudio` then `pip install pyaudio`
- Linux: `sudo apt-get install portaudio19-dev` then `pip install pyaudio`

### Frontend Issues

**"npm: command not found"**
- Install Node.js from https://nodejs.org/

**"Port 3000 already in use"**
- Stop other applications using port 3000
- Or use `PORT=3001 npm start` to use different port

**"Failed to fetch" errors**
- Make sure backend is running on port 5000
- Check `http://localhost:5000/api/health` in browser

### Microphone Issues

**Microphone not working**
- Grant microphone permissions in browser
- Click the 🔒 lock icon in address bar → Permissions → Microphone → Allow

**Voice recognition not accurate**
- Speak clearly and slowly
- Reduce background noise
- Make sure you're using Chrome (best support)

## Production Deployment

### Deploy Backend (Render.com - Free)

1. Create account on [Render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && gunicorn app:app`
   - **Environment Variables**: Add `GEMINI_API_KEY`
5. Click "Create Web Service"

### Deploy Frontend (Vercel - Free)

1. Install Vercel CLI: `npm install -g vercel`
2. Navigate to frontend: `cd frontend`
3. Run: `vercel`
4. Update `package.json` proxy to your backend URL

OR use [Vercel Dashboard](https://vercel.com):
- Import repository
- Set root directory to `frontend`
- Add environment variable `REACT_APP_API_URL` with backend URL

### Smart Board Deployment

1. Deploy both backend and frontend
2. On smart board browser, visit frontend URL
3. Press F11 for fullscreen
4. Grant microphone permissions
5. Done! 🎉

## Development Tips

### Backend Development

```bash
# Watch for changes (install flask-reload)
pip install flask-reload
FLASK_ENV=development python app.py
```

### Frontend Development

```bash
# Build for production
npm run build

# Test production build
npm install -g serve
serve -s build
```

## Project Structure

```
voice-teaching-assistant/
├── backend/
│   ├── app.py              # Flask server
│   ├── utils/
│   │   ├── ai_teacher.py   # Gemini integration
│   │   ├── quiz_generator.py
│   │   └── voice_handler.py
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── components/
│   │   │   ├── Home.js
│   │   │   ├── ExplainMode.js
│   │   │   └── QuizMode.js
│   │   └── index.js
│   ├── package.json
│   └── public/
└── README.md
```

## API Costs

**Google Gemini API (Free Tier):**
- 60 requests per minute
- 1,500 requests per day
- Perfect for classroom use!

For a school with 50 students:
- ~500 requests/day
- Well within free limits ✅

## Next Steps

1. ✅ Set up backend
2. ✅ Set up frontend
3. ✅ Test locally
4. 🚀 Deploy to production
5. 📹 Record demo video
6. 📝 Update README with live URL

## Support

Having issues? Check:
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://react.dev/)

Good luck with your project! 🎓🚀
