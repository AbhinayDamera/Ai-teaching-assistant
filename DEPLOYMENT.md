# Deployment Guide for Voice-Enabled AI Teaching Assistant

## Quick Start (Local Testing)

### 1. Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Windows (CMD)
venv\Scripts\activate.bat
# Linux/Mac
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

**Note for PyAudio on Windows:**
If PyAudio installation fails, download the wheel file:
```bash
pip install pipwin
pipwin install pyaudio
```

### 2. Configure API Keys

Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

Get your API key from: https://platform.openai.com/api-keys

### 3. Test Audio System

```bash
python test_audio.py
```

This will check if microphone and speakers are working properly.

### 4. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Smart Board Deployment

### Option 1: Local Network Access

1. Find your computer's IP address:
   ```bash
   # Windows
   ipconfig
   # Linux/Mac
   ifconfig
   ```

2. Run Streamlit with network access:
   ```bash
   streamlit run app.py --server.address 0.0.0.0 --server.port 8501
   ```

3. On the smart board browser, navigate to:
   ```
   http://<your-computer-ip>:8501
   ```

4. Press F11 for fullscreen mode

### Option 2: Cloud Deployment (Streamlit Cloud)

1. Push code to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/voice-teaching-assistant.git
   git push -u origin main
   ```

2. Go to [Streamlit Cloud](https://streamlit.io/cloud)

3. Sign in with GitHub

4. Click "New app" and select your repository

5. Add secrets (Settings → Secrets):
   ```toml
   OPENAI_API_KEY = "sk-your-actual-api-key-here"
   ```

6. Deploy and get your public URL

7. Access from smart board browser

### Option 3: Heroku Deployment

1. Create `Procfile`:
   ```
   web: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
   ```

2. Create `runtime.txt`:
   ```
   python-3.9.18
   ```

3. Deploy:
   ```bash
   heroku login
   heroku create voice-teaching-assistant
   heroku config:set OPENAI_API_KEY=your-api-key
   git push heroku main
   heroku open
   ```

## Mobile Access

The app is responsive and works on mobile devices:

1. Make sure computer and mobile are on same network

2. Access via: `http://<computer-ip>:8501`

3. Grant microphone permissions when prompted

4. Use in landscape mode for better experience

## Production Considerations

### Performance Optimization

1. **Caching**: Enable Streamlit caching for API calls
   ```python
   @st.cache_data(ttl=3600)
   def get_explanation(topic):
       # API call here
   ```

2. **Rate Limiting**: Implement rate limiting for API calls

3. **Fallback Mode**: Provide offline functionality for common topics

### Security

1. **API Key Security**:
   - Never commit `.env` to git
   - Use environment variables in production
   - Rotate keys regularly

2. **Input Validation**:
   - Already implemented in the code
   - Content filtering for inappropriate queries

3. **Network Security**:
   - Use HTTPS in production
   - Implement authentication for teacher dashboard
   - Use firewall rules to restrict access

### Monitoring

1. **Logs**: Check Streamlit logs for errors
   ```bash
   streamlit run app.py --server.runOnSave true 2>&1 | tee app.log
   ```

2. **API Usage**: Monitor OpenAI API usage dashboard

3. **User Feedback**: Add feedback collection mechanism

## Troubleshooting

### Microphone Issues

**Problem**: Microphone not detected
- **Solution**: 
  - Check browser permissions (click lock icon in address bar)
  - Try different browser (Chrome recommended)
  - Check system microphone settings

**Problem**: Poor recognition accuracy
- **Solution**:
  - Reduce background noise
  - Speak closer to microphone
  - Adjust energy threshold in code:
    ```python
    self.recognizer.energy_threshold = 3000  # Try different values
    ```

### Audio Playback Issues

**Problem**: TTS audio not playing
- **Solution**:
  - Enable autoplay in browser settings
  - Check volume settings
  - Try clicking "Allow audio" if prompted

### API Issues

**Problem**: OpenAI API errors
- **Solution**:
  - Verify API key is correct
  - Check API quota and billing
  - Implement retry logic with exponential backoff

### Performance Issues

**Problem**: Slow response times
- **Solution**:
  - Check internet connection speed
  - Use lower quality images (512x512 instead of 1024x1024)
  - Reduce max_tokens in API calls
  - Enable response caching

### Network Issues

**Problem**: Cannot access from smart board
- **Solution**:
  - Verify both devices on same network
  - Check firewall settings
  - Try disabling VPN
  - Use IP address instead of hostname

## Cost Optimization

### OpenAI API Costs (Approximate)

- **GPT-4**: ~$0.03 per explanation (750 tokens)
- **Whisper**: ~$0.006 per minute of audio
- **DALL-E 3**: ~$0.04 per image (standard quality)
- **TTS**: Free (using gTTS)

### Estimated Monthly Costs

**Small School** (100 queries/day):
- 3,000 explanations: $90
- 500 minutes audio: $3
- 500 images: $20
- **Total**: ~$113/month

**Tips to Reduce Costs**:
1. Use GPT-3.5-turbo instead of GPT-4 ($0.002 vs $0.03)
2. Cache common explanations
3. Generate images only when helpful
4. Use smaller image sizes (1024x1024 → 512x512)
5. Implement daily/weekly usage limits

## Alternative Free Options

If OpenAI costs are prohibitive:

1. **STT**: Use Google Speech Recognition (free, already in code)
2. **TTS**: Use gTTS (free, already in code)
3. **LLM**: Use free alternatives:
   - Hugging Face Inference API
   - Local models (Llama 2, Mistral)
   - Google Gemini API (free tier)
4. **Images**: Use free alternatives:
   - Stable Diffusion (self-hosted)
   - Bing Image Creator
   - Pre-generated diagram library

## Offline Mode (Future Enhancement)

For schools with unreliable internet:

1. Pre-download common explanations
2. Use local LLM (Llama, GPT4All)
3. Cache generated images
4. Implement progressive web app (PWA)

## Support

For technical support:
- GitHub Issues: Create an issue on the repository
- Email: support@example.com
- Documentation: Check README.md and code comments

## Updates

Check for updates regularly:
```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

## Backup and Recovery

1. **Backup conversation history**:
   - Logs stored in `.streamlit/logs/`
   - Export feature coming soon

2. **Configuration backup**:
   - Keep `.env` backed up securely
   - Document any custom configurations

---

**Remember**: This is educational technology. Always test thoroughly before deploying in live classroom environment!
