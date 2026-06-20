# 🎓 Voice-Enabled AI Teaching Assistant

**Interactive voice-based educational tool for Haryana government schools**

[![React](https://img.shields.io/badge/React-18.2-blue.svg)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-AI-orange.svg)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🎯 Problem Statement

Teachers in Haryana government schools need a hands-free AI co-pilot for live classroom sessions that:
- Works with smart boards
- Supports Hinglish (Hindi + English mix)
- Provides voice-based interactions
- Generates visual educational content

## ✨ Features Implemented

### 1. 🧠 Live Concept Simplification
- Voice or text input in Hinglish
- Real-time AI explanations using Google Gemini
- Text-to-speech output in Hindi
- Conversation history tracking
- Smart board optimized interface

### 2. 📝 Voice-Triggered Quizzing
- Generate quizzes on any topic
- Multiple choice questions in Hinglish
- Instant feedback with explanations
- Score tracking and performance summary
- Smooth animations and transitions

## 🛠️ Tech Stack

### Frontend
- **React 18** - Modern UI library
- **Framer Motion** - Smooth animations
- **Axios** - API communication
- **Lucide React** - Beautiful icons
- **CSS3** - Responsive design

### Backend
- **Flask** - Lightweight Python web framework
- **Google Gemini API** - Advanced AI for explanations
- **gTTS** - Text-to-speech (Hindi support)
- **SpeechRecognition** - Voice input processing
- **Flask-CORS** - Cross-origin support

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- Google Gemini API key ([Get it free](https://makersuite.google.com/app/apikey))

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/voice-teaching-assistant.git
cd voice-teaching-assistant
```

### 2. Setup Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Add your GEMINI_API_KEY to .env

python app.py
```

### 3. Setup Frontend
```bash
cd frontend
npm install
npm start
```

Visit `http://localhost:3000` 🎉

**For detailed setup instructions, see [SETUP.md](SETUP.md)**

## 📱 How to Use

### Explain Concept Mode
1. Click "Explain Concept"
2. Type your question OR hold mic button and speak
3. Get instant explanation in Hinglish
4. Listen to voice response

### Quiz Mode
1. Click "Quiz Mode"
2. Enter a topic (e.g., "Photosynthesis")
3. Answer 5 multiple-choice questions
4. See your score and explanations

## 🎨 UI/UX Features

- **Gradient Design** - Modern, attractive interface
- **Smooth Animations** - Page transitions and interactions
- **Responsive Layout** - Works on desktop, tablet, smart boards
- **Large Touch Targets** - Easy to use on touch screens
- **Visual Feedback** - Loading states, success/error indicators
- **Bilingual** - English + Hindi throughout interface

## 🎯 Smart Board Optimization

- **Fullscreen Mode** - Press F11 for immersive experience
- **Large Fonts** - Easy to read from distance
- **High Contrast** - Clear visibility
- **Touch-Friendly** - Big buttons (60px+ height)
- **Voice-First** - Hands-free operation

## 📊 Project Structure

```
voice-teaching-assistant/
├── backend/                 # Flask API server
│   ├── app.py              # Main Flask app
│   ├── utils/
│   │   ├── ai_teacher.py   # Gemini integration
│   │   ├── quiz_generator.py
│   │   └── voice_handler.py
│   └── requirements.txt
├── frontend/                # React application
│   ├── src/
│   │   ├── App.js
│   │   ├── components/
│   │   │   ├── Home.js
│   │   │   ├── ExplainMode.js
│   │   │   └── QuizMode.js
│   │   └── index.js
│   └── package.json
├── README.md
└── SETUP.md
```

## 🎓 Prompt Design

### Educational Guardrails
- Age-appropriate content (grades 6-10)
- Simple Hinglish language
- Indian cultural context
- Real-life examples (farms, markets, cricket)
- Encouraging and supportive tone
- Strict educational focus

### Hinglish Optimization
- Natural Hindi-English mix
- Roman script only (no Devanagari)
- Common Hindi words: samjho, dekho, hai, kaise, kyun
- Short sentences for clarity

### Example Interaction
```
User: "Photosynthesis kya hai?"

AI: "🌿 Simple answer: Plants sunlight se apna khana banate hain!

Explanation: Jaise hum roti pakane ke liye aag chahiye, waise plants 
ko sunlight chahiye. Plants pani + CO2 + sunlight le kar glucose 
(meetha khana) banate hain aur oxygen release karte hain.

💡 Yaad rakhne ki trick: Photo = Light, Synthesis = Banana. 
Bas yaad rakho 'Sunlight se khana banana'!"
```

## 🌍 Localization

- **Primary Language**: Hinglish (Hindi + English)
- **Script**: Roman/Latin for wider compatibility
- **Voice Input**: Accepts Hindi and English
- **Voice Output**: Natural Hindi-accented speech
- **Visual Text**: Bilingual labels

## 💰 Cost Analysis

### Google Gemini API (Free Tier)
- **Limits**: 60 requests/min, 1,500 requests/day
- **Perfect for classroom use!**

### Estimated Usage (50 students/day)
- ~500 API requests/day
- Well within free limits ✅
- **Total Cost**: ₹0/month

### Alternative (Paid)
If scaling to multiple schools:
- Google Gemini Pro: ~$0.0005 per request
- 10,000 requests = $5/month
- Still very affordable!

## 🔒 Safety & Privacy

- No student data stored permanently
- Voice processed in real-time and discarded
- Content filtering for inappropriate queries
- Teacher override controls
- HTTPS encryption in production

## 🚀 Deployment

### Option 1: Render.com + Vercel (Recommended - Free)
- Backend: Render.com (Flask)
- Frontend: Vercel (React)
- See [SETUP.md](SETUP.md) for step-by-step

### Option 2: Local Network
- Run on teacher's laptop
- Access via smart board browser
- Use local IP address

### Option 3: Heroku
- Single platform deployment
- Easy scaling

## 📈 Future Enhancements

- [ ] Image generation for concepts (DALL-E integration)
- [ ] Multi-language support (Punjabi, Tamil)
- [ ] Offline mode with cached responses
- [ ] Teacher dashboard for tracking
- [ ] Student progress analytics
- [ ] Whiteboard integration
- [ ] Mobile app (React Native)

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 🐛 Troubleshooting

### Microphone Issues
- Grant browser microphone permissions
- Use Chrome for best compatibility
- Check system microphone settings

### API Errors
- Verify Gemini API key in `.env`
- Check API quota at Google AI Studio
- Ensure backend is running

### Connection Issues
- Verify backend runs on port 5000
- Check frontend proxy configuration
- Disable VPN if connection fails

**More help in [SETUP.md](SETUP.md)**

## 📄 License

MIT License - See [LICENSE](LICENSE) file

## 👥 Authors

Built for **Haryana Government Schools Initiative**

## 🙏 Acknowledgments

- Google Gemini for free AI API
- React and Flask communities
- Haryana Education Department
- Open source contributors

## 📞 Support

- **Email**: your.email@example.com
- **Issues**: [GitHub Issues](https://github.com/yourusername/voice-teaching-assistant/issues)
- **Documentation**: See SETUP.md

---

**Made with ❤️ for Indian education** 🇮🇳

**Live Demo**: [Coming Soon]  
**Video Walkthrough**: [Coming Soon]

---

### 📸 Screenshots

*Add screenshots of your app here after running it*

1. Home Screen
2. Explain Mode
3. Quiz Mode
4. Results Screen
