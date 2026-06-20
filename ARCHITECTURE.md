# 🏗️ System Architecture

## High-Level Overview

```
┌─────────────────────────────────────────────────────────────┐
│                         USER                                │
│              (Teacher/Student with Smart Board)             │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       │ HTTP/Voice
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                  FRONTEND (React)                           │
│  ┌────────────┐  ┌─────────────┐  ┌──────────────────┐    │
│  │   Home     │  │  Explain    │  │   Quiz Mode      │    │
│  │  Component │  │   Mode      │  │                  │    │
│  └────────────┘  └─────────────┘  └──────────────────┘    │
│                                                             │
│  - Voice Capture (Browser API)                             │
│  - Smooth Animations (Framer Motion)                       │
│  - Responsive UI (CSS3)                                    │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       │ REST API (Axios)
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                  BACKEND (Flask)                            │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐  │
│  │              API Routes (app.py)                    │  │
│  │  • /api/health                                      │  │
│  │  • /api/explain                                     │  │
│  │  • /api/quiz/generate                               │  │
│  │  • /api/tts (text-to-speech)                        │  │
│  │  • /api/stt (speech-to-text)                        │  │
│  └──────────┬────────────────────────────┬───────────────┘  │
│             │                            │                  │
│  ┌──────────▼──────────┐    ┌───────────▼──────────────┐  │
│  │   AI Teacher        │    │   Quiz Generator         │  │
│  │  (ai_teacher.py)    │    │  (quiz_generator.py)     │  │
│  │                     │    │                          │  │
│  │  • System Prompt    │    │  • System Prompt         │  │
│  │  • Gemini API Call  │    │  • JSON Generation       │  │
│  │  • Error Handling   │    │  • Fallback Quiz         │  │
│  └──────────┬──────────┘    └───────────┬──────────────┘  │
│             │                            │                  │
│  ┌──────────▼────────────────────────────▼──────────────┐  │
│  │           Voice Handler                              │  │
│  │         (voice_handler.py)                           │  │
│  │  • Speech Recognition                                │  │
│  │  • Text-to-Speech (gTTS)                             │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       │ HTTPS API
                       │
┌──────────────────────▼──────────────────────────────────────┐
│              GOOGLE GEMINI API                              │
│  • gemini-1.5-flash model                                   │
│  • Free tier: 1,500 requests/day                            │
│  • Response time: 1-3 seconds                               │
│  • Native Hindi/Hinglish support                            │
└─────────────────────────────────────────────────────────────┘
```

## Component Details

### Frontend Layer (React)

```
src/
├── App.js                    Main app with routing logic
│   └── AnimatePresence       Smooth page transitions
│
├── components/
│   ├── Home.js              Landing page
│   │   ├── Mode selection cards
│   │   ├── Gradient designs
│   │   └── Motion animations
│   │
│   ├── ExplainMode.js       Concept explanation
│   │   ├── Text input
│   │   ├── Voice recording (MediaRecorder API)
│   │   ├── API call to /api/explain
│   │   ├── Display answer
│   │   ├── TTS playback
│   │   └── History tracking
│   │
│   └── QuizMode.js          Quiz interface
│       ├── Topic input
│       ├── API call to /api/quiz/generate
│       ├── Question display
│       ├── Answer selection
│       ├── Instant feedback
│       └── Score calculation
```

### Backend Layer (Flask)

```
backend/
├── app.py                   Flask server
│   ├── CORS configuration
│   ├── Route definitions
│   └── Error handling
│
└── utils/
    ├── ai_teacher.py        Gemini integration
    │   ├── System prompt engineering
    │   ├── generate_content() call
    │   └── Response formatting
    │
    ├── quiz_generator.py    Quiz creation
    │   ├── JSON generation
    │   ├── Question validation
    │   └── Fallback quizzes
    │
    └── voice_handler.py     Voice I/O
        ├── Google Speech Recognition
        ├── gTTS (Google Text-to-Speech)
        └── Audio file handling
```

## Data Flow

### Explain Mode Flow

```
1. User Action
   └─> Type or speak question

2. Frontend Processing
   └─> If voice: MediaRecorder → Blob → FormData
   └─> If text: Direct string

3. API Request
   └─> POST /api/explain
       {
         "question": "What is photosynthesis?"
       }

4. Backend Processing
   └─> AITeacher.explain_concept()
       └─> Gemini API call
           └─> System prompt + user question
               └─> Hinglish response

5. Response
   └─> {
         "explanation": "Photosynthesis ek aisa process...",
         "error": false
       }

6. Frontend Display
   └─> Show explanation in styled box
   └─> Call /api/tts for voice output
       └─> Play audio

7. User hears and sees answer
```

### Quiz Mode Flow

```
1. User enters topic
   └─> "Fractions"

2. API Request
   └─> POST /api/quiz/generate
       {
         "topic": "Fractions",
         "num_questions": 5
       }

3. Backend Processing
   └─> QuizGenerator.generate_quiz()
       └─> Gemini API call
           └─> JSON response requested
               └─> {
                     "topic": "Fractions",
                     "questions": [...]
                   }

4. Frontend Receives Quiz
   └─> Store in state
   └─> Display first question

5. User selects answer
   └─> Frontend validates locally
   └─> Show green/red feedback
   └─> Display explanation

6. Continue until all questions
   └─> Show final score
   └─> Offer to restart
```

## API Endpoints

### GET /api/health
**Purpose**: Check if backend is running  
**Request**: None  
**Response**:
```json
{
  "status": "healthy",
  "message": "Voice Teaching Assistant API"
}
```

### POST /api/explain
**Purpose**: Get AI explanation for a concept  
**Request**:
```json
{
  "question": "string"
}
```
**Response**:
```json
{
  "explanation": "string (Hinglish)",
  "error": false
}
```

### POST /api/quiz/generate
**Purpose**: Generate quiz on a topic  
**Request**:
```json
{
  "topic": "string",
  "num_questions": 5
}
```
**Response**:
```json
{
  "topic": "string",
  "questions": [
    {
      "question": "string",
      "options": ["A", "B", "C", "D"],
      "correct": 0,
      "explanation": "string"
    }
  ]
}
```

### POST /api/tts
**Purpose**: Convert text to speech  
**Request**:
```json
{
  "text": "string",
  "lang": "hi"
}
```
**Response**:
```json
{
  "audio": "base64_encoded_mp3",
  "format": "mp3"
}
```

### POST /api/stt
**Purpose**: Convert speech to text  
**Request**: FormData with audio file  
**Response**:
```json
{
  "text": "string"
}
```

## Technology Stack Details

### Frontend
| Technology | Version | Purpose |
|------------|---------|---------|
| React | 18.2 | UI library |
| Framer Motion | 10.16 | Animations |
| Axios | 1.6 | HTTP client |
| Lucide React | 0.294 | Icons |
| Browser MediaRecorder | Native | Voice recording |

### Backend
| Technology | Version | Purpose |
|------------|---------|---------|
| Flask | 3.0 | Web framework |
| google-generativeai | 0.3+ | Gemini API |
| gTTS | 2.5 | Text-to-speech |
| SpeechRecognition | 3.10 | Voice input |
| Flask-CORS | 4.0 | Cross-origin |

### External Services
| Service | Purpose | Cost |
|---------|---------|------|
| Google Gemini | AI responses | Free (1,500/day) |
| Google Speech API | Voice recognition | Free |
| gTTS | Text-to-speech | Free |

## Security Considerations

### Frontend
- ✅ CORS configured properly
- ✅ Input sanitization
- ✅ No sensitive data in localStorage
- ✅ Microphone permissions required

### Backend
- ✅ Environment variables for secrets
- ✅ API key not exposed to frontend
- ✅ Rate limiting (Gemini's built-in)
- ✅ Input validation
- ✅ Error messages sanitized

### API
- ✅ HTTPS required in production
- ✅ No API key in response
- ✅ Content filtering in prompts
- ✅ Educational content only

## Performance Optimizations

### Frontend
- ⚡ Code splitting (React.lazy)
- ⚡ Lazy loading components
- ⚡ Debounced voice input
- ⚡ Optimized animations
- ⚡ Minimal re-renders

### Backend
- ⚡ Efficient API calls
- ⚡ Response caching (future)
- ⚡ Async operations
- ⚡ Connection pooling
- ⚡ Gzip compression

### API Usage
- ⚡ Batch requests where possible
- ⚡ Fallback responses
- ⚡ Retry with exponential backoff
- ⚡ Request timeouts

## Scalability

### Current Limits
- **Gemini Free**: 1,500 requests/day
- **Concurrent Users**: ~50 simultaneous
- **Response Time**: 1-3 seconds

### Scaling Options

**Option 1: Vertical Scaling**
- Upgrade to Gemini Pro
- Better server (more RAM/CPU)
- Cost: ~$50/month for 200 students/day

**Option 2: Horizontal Scaling**
- Multiple backend instances
- Load balancer
- Redis for caching
- Cost: ~$100/month for 1,000 students/day

**Option 3: Hybrid**
- Cache common questions
- Fallback to local model
- Use Gemini for complex queries
- Cost: ~$20/month for 500 students/day

## Monitoring & Logging

### Frontend
- Browser console errors
- Performance metrics (Web Vitals)
- User interaction tracking
- API response times

### Backend
- Flask logs
- API usage statistics
- Error rates
- Response times
- Gemini quota tracking

## Future Architecture Enhancements

### Phase 2
```
├── Redis Cache
│   └── Common Q&A pairs
├── PostgreSQL Database
│   └── User progress tracking
├── WebSocket
│   └── Real-time collaboration
```

### Phase 3
```
├── Microservices
│   ├── Auth Service
│   ├── Analytics Service
│   └── Content Service
├── CDN
│   └── Static assets
├── Message Queue
│   └── Async job processing
```

---

## Quick Reference

**Frontend Port**: 3000  
**Backend Port**: 5000  
**API Base**: http://localhost:5000/api  
**Proxy**: Configured in package.json  

**Main Files**:
- Frontend: `frontend/src/App.js`
- Backend: `backend/app.py`
- AI: `backend/utils/ai_teacher.py`

**Key Commands**:
```bash
# Start backend
cd backend && python app.py

# Start frontend
cd frontend && npm start

# Test backend
cd backend && python test_api.py
```

---

*For more details, see [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)*
