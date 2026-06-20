# 🚀 Deployment Guide

## Stack
- **Backend** → Render.com (Free)
- **Frontend** → Vercel (Free)

---

## STEP 1: Push Code to GitHub

### 1.1 Create a GitHub account
Go to https://github.com and sign up (free)

### 1.2 Create a new repository
- Click "+" → "New repository"
- Name: `ai-teaching-assistant`
- Set to **Public**
- Click "Create repository"

### 1.3 Push your code
Run these commands in your project root folder:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-teaching-assistant.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

---

## STEP 2: Deploy Backend on Render

### 2.1 Go to Render
Visit https://render.com → Sign up with GitHub

### 2.2 Create new Web Service
- Click **"New +"** → **"Web Service"**
- Connect your GitHub repo: `ai-teaching-assistant`
- Configure:

| Setting | Value |
|---------|-------|
| **Name** | `ai-teaching-assistant-backend` |
| **Root Directory** | `backend` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| **Instance Type** | `Free` |

### 2.3 Add Environment Variable
- Scroll to **"Environment Variables"**
- Click **"Add Environment Variable"**
- Key: `GEMINI_API_KEY`
- Value: `your_actual_gemini_api_key`

### 2.4 Click "Create Web Service"
- Wait 3-5 minutes for deployment
- You'll get a URL like: `https://ai-teaching-assistant-backend.onrender.com`
- **Copy this URL!** You'll need it in Step 3.

### 2.5 Test your backend
Visit: `https://your-backend-url.onrender.com/api/health`

You should see:
```json
{"status": "healthy", "message": "Voice Teaching Assistant API"}
```

---

## STEP 3: Deploy Frontend on Vercel

### 3.1 Go to Vercel
Visit https://vercel.com → Sign up with GitHub

### 3.2 Import Project
- Click **"New Project"**
- Import your GitHub repo: `ai-teaching-assistant`
- Configure:

| Setting | Value |
|---------|-------|
| **Root Directory** | `frontend` |
| **Framework Preset** | `Create React App` |
| **Build Command** | `npm run build` |
| **Output Directory** | `build` |

### 3.3 Add Environment Variable
- Click **"Environment Variables"**
- Add:

| Name | Value |
|------|-------|
| `REACT_APP_API_URL` | `https://your-backend-url.onrender.com` |

⚠️ Replace with your actual Render URL from Step 2.4

### 3.4 Click "Deploy"
- Wait 2-3 minutes
- You'll get a URL like: `https://ai-teaching-assistant.vercel.app`
- **This is your live app URL!** 🎉

---

## STEP 4: Test Live App

1. Visit your Vercel URL
2. Check landing page loads
3. Click "Get Started · शुरू करें →"
4. Try Explain Mode with a question
5. Try Quiz Mode with a topic

---

## 🐛 Troubleshooting

### Backend shows "Application Error"
- Check Render logs (Dashboard → your service → "Logs")
- Verify `GEMINI_API_KEY` is set correctly
- Make sure `requirements.txt` has no `PyAudio`

### Frontend shows "Failed to fetch"
- Check `REACT_APP_API_URL` in Vercel env variables
- Make sure the URL doesn't have a trailing slash
- Verify backend is running on Render

### Quiz/Explain not working
- Open browser DevTools (F12) → Console tab
- Check for CORS errors
- Verify backend URL is correct

### Render backend is slow (cold start)
- Free tier goes to sleep after 15 min of inactivity
- First request takes 30-60 seconds to wake up
- This is normal on the free plan

---

## 📝 After Deployment

Update your README.md with:
```markdown
## 🌐 Live Demo
- Frontend: https://your-app.vercel.app
- Backend API: https://your-backend.onrender.com
```

---

## 💰 Cost
| Service | Cost |
|---------|------|
| Render (backend) | **FREE** (750 hrs/month) |
| Vercel (frontend) | **FREE** (unlimited) |
| Gemini API | **FREE** (1500 requests/day) |
| **Total** | **₹0/month** |
