# ⚡ Quick Start Guide

Get your Voice Teaching Assistant running in **5 minutes**!

## 📋 Before You Start

Make sure you have:
- ✅ Python 3.9+ installed
- ✅ Node.js 16+ installed
- ✅ Google Gemini API key ([Get it FREE here](https://makersuite.google.com/app/apikey))

## 🚀 Installation (First Time Only)

### Step 1: Backend Setup

```bash
# Go to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install Python packages
pip install -r requirements.txt
```

**Windows PyAudio Issue?**
```bash
pip install pipwin
pipwin install pyaudio
```

### Step 2: Add Your API Key

```bash
# In backend folder, copy the example
copy .env.example .env      # Windows
# OR
cp .env.example .env        # Mac/Linux

# Edit .env file and add your Gemini API key:
GEMINI_API_KEY=your_actual_key_here
```

### Step 3: Frontend Setup

```bash
# Go to frontend folder (open NEW terminal)
cd frontend

# Install Node packages
npm install
```

## ▶️ Running the App

### Option 1: Manual Start

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python app.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```

### Option 2: Quick Start Script

**Windows:**
```bash
start.bat
```

**Mac/Linux:**
```bash
chmod +x start.sh
./start.sh
```

## 🎉 You're Done!

The app will open automatically at `http://localhost:3000`

### Now Try:
1. Click **"Explain Concept"**
2. Type: "What is photosynthesis?"
3. Get instant AI explanation!

OR

1. Click **"Quiz Mode"**
2. Type topic: "Fractions"
3. Answer quiz questions!

## 🎤 Voice Input

1. Click the mic button
2. **Hold it down** while speaking
3. Release when done
4. Your speech will be converted to text

**Note:** Grant microphone permissions when browser asks!

## 🐛 Quick Fixes

### "Module not found" error
```bash
cd backend
pip install -r requirements.txt
```

### "npm command not found"
Install Node.js from: https://nodejs.org/

### "Port 5000 already in use"
Kill the process:
```bash
# Windows:
netstat -ano | findstr :5000
taskkill /PID <process_id> /F

# Mac/Linux:
lsof -ti:5000 | xargs kill -9
```

### Microphone not working
1. Click 🔒 lock icon in browser address bar
2. Permissions → Microphone → Allow
3. Refresh page

## 📂 Project Structure

```
voice-teaching-assistant/
├── backend/              ← Flask API
│   ├── app.py
│   ├── utils/
│   └── requirements.txt
├── frontend/             ← React UI
│   ├── src/
│   ├── public/
│   └── package.json
├── start.bat            ← Windows quick start
├── start.sh             ← Mac/Linux quick start
├── QUICK_START.md       ← You are here!
├── SETUP.md             ← Detailed setup
└── README.md            ← Full documentation
```

## 🎯 Next Steps

1. ✅ Run the app locally
2. 📹 Record a demo video (max 3 mins)
3. 🚀 Deploy to cloud (see SETUP.md)
4. 📝 Add screenshots to README.md
5. 🌐 Share your GitHub repo

## 💡 Pro Tips

**For Smart Board:**
- Press **F11** for fullscreen
- Increase browser zoom to 125%
- Use external USB microphone for better recognition

**For Development:**
- Backend auto-reloads on code changes
- Frontend hot-reloads automatically
- Use Chrome DevTools for debugging

## 📚 Learn More

- **Full Setup Guide**: [SETUP.md](SETUP.md)
- **Complete Docs**: [README.md](README.md)
- **API Reference**: Check `backend/app.py`

## 🆘 Need Help?

1. Check [SETUP.md](SETUP.md) troubleshooting section
2. Open GitHub issue
3. Email: support@example.com

---

**Happy Teaching! 🎓🚀**
