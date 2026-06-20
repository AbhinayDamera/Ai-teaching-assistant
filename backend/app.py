from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from dotenv import load_dotenv
from utils.ai_teacher import AITeacher
from utils.quiz_generator import QuizGenerator
from utils.voice_handler import VoiceHandler
import tempfile
import base64

load_dotenv()

app = Flask(__name__)

# Allow all origins in production (update with your Vercel URL for security)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Initialize services
ai_teacher = AITeacher()
quiz_generator = QuizGenerator()
voice_handler = VoiceHandler()

@app.route('/api/health', methods=['GET'])
def health_check():
    """Check if API is running"""
    return jsonify({"status": "healthy", "message": "Voice Teaching Assistant API"})

@app.route('/api/explain', methods=['POST'])
def explain_concept():
    """Explain a concept in Hinglish"""
    try:
        data = request.json
        question = data.get('question', '')
        
        if not question:
            return jsonify({"error": "Question is required"}), 400
        
        result = ai_teacher.explain_concept(question)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/quiz/generate', methods=['POST'])
def generate_quiz():
    """Generate a quiz on a topic"""
    try:
        data = request.json
        topic = data.get('topic', '')
        num_questions = data.get('num_questions', 5)
        
        if not topic:
            return jsonify({"error": "Topic is required"}), 400
        
        quiz = quiz_generator.generate_quiz(topic, num_questions)
        return jsonify(quiz)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/tts', methods=['POST'])
def text_to_speech():
    """Convert text to speech and return audio"""
    try:
        data = request.json
        text = data.get('text', '')
        lang = data.get('lang', 'hi')
        
        if not text:
            return jsonify({"error": "Text is required"}), 400
        
        audio_data = voice_handler.text_to_speech(text, lang)
        
        if audio_data:
            # Return audio as base64
            audio_base64 = base64.b64encode(audio_data).decode('utf-8')
            return jsonify({
                "audio": audio_base64,
                "format": "mp3"
            })
        else:
            return jsonify({"error": "TTS failed"}), 500
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/stt', methods=['POST'])
def speech_to_text():
    """Convert speech to text (expects audio file)"""
    try:
        if 'audio' not in request.files:
            return jsonify({"error": "Audio file is required"}), 400
        
        audio_file = request.files['audio']
        
        # Save temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
            audio_file.save(temp_audio.name)
            text = voice_handler.recognize_audio_file(temp_audio.name)
            os.unlink(temp_audio.name)
        
        if text:
            return jsonify({"text": text})
        else:
            return jsonify({"error": "Could not recognize speech"}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
