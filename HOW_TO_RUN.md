# 🎯 How to Run This Project

## Quick Summary

This project has **2 parts**:
1. **Backend** (Flask + Python) - Handles AI and voice processing
2. **Frontend** (React) - Beautiful user interface

Both need to run simultaneously.

---

## 🚀 First Time Setup (Do Once)

### 1. Get Google Gemini API Key (FREE)
- Visit: https://makersuite.google.com/app/apikey
- Sign in with Google
- Click "Create API Key"
- Copy the key (starts with `AIza...`)

### 2. Install Backend

```bash
cd backend
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

**Windows PyAudio issue?**
```bash
pip install pipwin
pipwin install pyaudio
```

### 3. Configure API Key

```bash
# Still in backend folder
copy .env.example .env      # Windows
# OR
cp .env.example .env        # Mac/Linux
```

Edit `.env` file:
```
GEMINI_API_KEY=your_actual_api_key_here
```

### 4. Install Frontend

```bash
# Open NEW terminal
cd frontend
npm install
```

---

## ▶️ Running the App (Every Time)

### Method 1: Automatic (Recommended)

**Windows:**
```bash
start.bat
```

**Mac/Linux:**
```bash
chmod +x start.sh
./start.sh
```

### Method 2: Manual (Two Terminals)

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
python app.py
```

Wait for: `* Running on http://127.0.0.1:5000`

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```

Browser will open automatically at `http://localhost:3000`

---

## ✅ Verify It's Working

### Test Backend
```bash
cd backend
python test_api.py
```

Should see:
```
✅ Backend is healthy!
✅ Explain endpoint working!
✅ Quiz endpoint working!
```

### Test Frontend
- Open `http://localhost:3000` in browser
- You should see 2 colorful cards:
  - "Explain Concept"
  - "Quiz Mode"

---

## 🎮 How to Use

### Explain Mode
1. Click "Explain Concept"
2. Type a question: "What is photosynthesis?"
3. OR hold mic button and speak
4. Get AI explanation with voice

### Quiz Mode
1. Click "Quiz Mode"
2. Type topic: "Fractions"
3. Click "Generate Quiz"
4. Answer 5 questions
5. See your score!

---

## 🐛 Common Issues

### "Backend not responding"
```bash
# Check if backend is running
# Should see Flask server on port 5000
netstat -an | grep 5000     # Mac/Linux
netstat -an | findstr 5000  # Windows
```

### "API Key Error"
- Check `backend/.env` file exists
- Verify key is correct (no quotes needed)
- Key should start with `AIza...`

### "Microphone not working"
1. Click 🔒 lock icon in browser
2. Allow microphone access
3. Refresh page

### "Port already in use"
```bash
# Kill process on port 5000
# Windows:
netstat -ano | findstr :5000
taskkill /PID <pid> /F

# Mac/Linux:
lsof -ti:5000 | xargs kill -9
```

---

## 📁 Project Structure

```
voice-teaching-assistant/
│
├── backend/                    ← Python Flask server
│   ├── app.py                  (main API)
│   ├── utils/
│   │   ├── ai_teacher.py       (Gemini integration)
│   │   ├── quiz_generator.py   (Quiz creation)
│   │   └── voice_handler.py    (Voice I/O)
│   ├── requirements.txt
│   ├── .env                    (YOUR API KEY)
│   └── test_api.py
│
├── frontend/                   ← React UI
│   ├── src/
│   │   ├── App.js
│   │   ├── components/
│   │   │   ├── Home.js
│   │   │   ├── ExplainMode.js
│   │   │   └── QuizMode.js
│   │   └── index.js
│   └── package.json
│
├── start.bat                   (Windows quick start)
├── start.sh                    (Mac/Linux quick start)
├── QUICK_START.md
├── SETUP.md
└── README.md
```

---

## 🎯 Development Workflow

```bash
# 1. Start backend (Terminal 1)
cd backend
source venv/bin/activate
python app.py

# 2. Start frontend (Terminal 2)
cd frontend
npm start

# 3. Make changes to code
# Both servers auto-reload!

# 4. Test backend
cd backend
python test_api.py

# 5. Build for production
cd frontend
npm run build
```

---

## 📚 More Documentation

- **Quick Start**: [QUICK_START.md](QUICK_START.md) - 5-minute setup
- **Full Setup**: [SETUP.md](SETUP.md) - Complete guide
- **Features**: [README.md](README.md) - Project overview

---

## 🆘 Still Having Issues?

1. Check logs in terminal windows
2. Try incognito/private browser window
3. Disable browser extensions
4. Check firewall settings
5. Create GitHub issue with error logs

---

## ✨ Tips

- Use **Chrome** for best microphone support
- **F11** for fullscreen on smart board
- Speak **clearly** and **slowly** for voice input
- Works best in **quiet** environment
- Allow 2-3 seconds for AI responses

---

**Enjoy building! 🚀🎓**
