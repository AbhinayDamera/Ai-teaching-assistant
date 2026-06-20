# ✅ Installation Checklist

Use this checklist to ensure everything is set up correctly.

## 📦 Prerequisites

- [ ] Python 3.9+ installed
  ```bash
  python --version
  # Should show 3.9 or higher
  ```

- [ ] Node.js 16+ installed
  ```bash
  node --version
  # Should show v16 or higher
  ```

- [ ] Git installed (for cloning repo)
  ```bash
  git --version
  ```

- [ ] Google Gemini API key obtained
  - Visit: https://makersuite.google.com/app/apikey
  - Save your key somewhere safe

## 🔧 Backend Setup

- [ ] Navigate to backend folder
  ```bash
  cd backend
  ```

- [ ] Create virtual environment
  ```bash
  python -m venv venv
  ```

- [ ] Activate virtual environment
  ```bash
  # Windows PowerShell:
  venv\Scripts\Activate.ps1
  # Windows CMD:
  venv\Scripts\activate.bat
  # Mac/Linux:
  source venv/bin/activate
  ```

- [ ] Install Python dependencies
  ```bash
  pip install -r requirements.txt
  ```

- [ ] Fix PyAudio if needed (Windows)
  ```bash
  pip install pipwin
  pipwin install pyaudio
  ```

- [ ] Create .env file
  ```bash
  # Windows:
  copy .env.example .env
  # Mac/Linux:
  cp .env.example .env
  ```

- [ ] Add Gemini API key to .env
  - Open `backend/.env` in text editor
  - Replace `your_gemini_api_key_here` with actual key
  - Save and close

- [ ] Test backend
  ```bash
  python test_api.py
  ```
  - Should see 3/3 tests passed ✅

## 🎨 Frontend Setup

- [ ] Open new terminal window

- [ ] Navigate to frontend folder
  ```bash
  cd frontend
  ```

- [ ] Install Node dependencies
  ```bash
  npm install
  ```
  - Wait for ~2-5 minutes depending on internet speed

- [ ] Verify package.json has proxy
  - Open `frontend/package.json`
  - Should see: `"proxy": "http://localhost:5000"`

## 🚀 Running the Application

- [ ] Start backend (Terminal 1)
  ```bash
  cd backend
  source venv/bin/activate  # or venv\Scripts\activate
  python app.py
  ```
  - Should see: `Running on http://127.0.0.1:5000`
  - Keep this terminal open

- [ ] Start frontend (Terminal 2)
  ```bash
  cd frontend
  npm start
  ```
  - Browser should open automatically
  - Should see app at `http://localhost:3000`

## ✅ Verification Tests

### Backend Tests

- [ ] Test API health
  - Visit: http://localhost:5000/api/health
  - Should see: `{"status": "healthy"}`

- [ ] Test explanation endpoint
  ```bash
  cd backend
  python test_api.py
  ```

### Frontend Tests

- [ ] Home page loads
  - See two colorful cards
  - "Explain Concept" and "Quiz Mode"

- [ ] Explain mode works
  - Click "Explain Concept"
  - Type: "What is water?"
  - Click "Ask"
  - Get response with explanation

- [ ] Quiz mode works
  - Click "Quiz Mode"
  - Type: "Science"
  - Click "Generate Quiz"
  - See 5 questions

### Voice Tests

- [ ] Microphone permissions granted
  - Browser should ask for permission
  - Click "Allow"

- [ ] Voice input works
  - In Explain mode
  - Hold mic button
  - Speak: "What is gravity?"
  - Release button
  - Text appears in input box

- [ ] Voice output works
  - After getting explanation
  - Click "Speak" button
  - Should hear Hindi voice

## 🎯 Optional Enhancements

- [ ] Test on different browsers
  - [ ] Chrome (recommended)
  - [ ] Firefox
  - [ ] Edge
  - [ ] Safari

- [ ] Test responsive design
  - [ ] Desktop (1920x1080)
  - [ ] Tablet (768px)
  - [ ] Mobile (375px)

- [ ] Performance check
  - [ ] Response time < 3 seconds
  - [ ] Smooth animations
  - [ ] No console errors

## 📱 Smart Board Setup (Optional)

- [ ] Find computer's local IP
  ```bash
  # Windows:
  ipconfig
  # Mac/Linux:
  ifconfig
  ```

- [ ] Start backend with network access
  ```bash
  python app.py
  # Already allows 0.0.0.0 by default
  ```

- [ ] Access from smart board
  - Open browser on smart board
  - Visit: `http://<your-ip>:3000`
  - Press F11 for fullscreen

## 🐛 Common Issues Resolved

### Issue: "Python not found"
- [ ] Verify Python installation
- [ ] Add Python to PATH
- [ ] Restart terminal

### Issue: "npm not found"
- [ ] Install Node.js from nodejs.org
- [ ] Restart terminal
- [ ] Verify with `node --version`

### Issue: "Port 5000 already in use"
- [ ] Find process using port
  ```bash
  # Windows:
  netstat -ano | findstr :5000
  taskkill /PID <pid> /F
  
  # Mac/Linux:
  lsof -ti:5000 | xargs kill -9
  ```

### Issue: "Module not found" errors
- [ ] Activate virtual environment first
- [ ] Re-run `pip install -r requirements.txt`

### Issue: "API key error"
- [ ] Check `.env` file exists in backend folder
- [ ] Verify key has no spaces or quotes
- [ ] Key should start with `AIza...`

### Issue: "Microphone not working"
- [ ] Grant browser permissions
- [ ] Check system microphone settings
- [ ] Try different browser (Chrome works best)

## 📊 Final Checklist

Before considering setup complete:

- [ ] Backend running without errors
- [ ] Frontend loads in browser
- [ ] Can ask questions and get answers
- [ ] Can generate quizzes
- [ ] Voice input works
- [ ] Voice output works
- [ ] No console errors in browser
- [ ] API key working (not seeing ⚠️ errors)

## 🎉 Success!

If all checkboxes are marked, congratulations! 🎊

You're ready to:
1. 📹 Record your demo video
2. 🚀 Deploy to cloud
3. 📝 Add screenshots to README
4. 🌐 Share your project

## 📚 Next Steps

- [ ] Read [QUICK_START.md](QUICK_START.md) for usage tips
- [ ] Read [SETUP.md](SETUP.md) for deployment guide
- [ ] Read [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for technical details
- [ ] Star the GitHub repo ⭐
- [ ] Share with other developers

---

**Need help?** Create an issue on GitHub or refer to [HOW_TO_RUN.md](HOW_TO_RUN.md)
