import speech_recognition as sr
from gtts import gTTS
import tempfile
import os

class VoiceHandler:
    """Handle speech-to-text and text-to-speech"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 4000
        self.recognizer.dynamic_energy_threshold = True
    
    def recognize_audio_file(self, audio_path: str) -> str:
        """Convert audio file to text"""
        try:
            with sr.AudioFile(audio_path) as source:
                audio = self.recognizer.record(source)
                
                # Try Hindi first
                try:
                    text = self.recognizer.recognize_google(audio, language="hi-IN")
                    return text
                except sr.UnknownValueError:
                    # Try English
                    try:
                        text = self.recognizer.recognize_google(audio, language="en-IN")
                        return text
                    except:
                        return None
        except Exception as e:
            print(f"Audio recognition error: {e}")
            return None
    
    def text_to_speech(self, text: str, lang: str = 'hi') -> bytes:
        """Convert text to speech, return audio bytes"""
        try:
            tts = gTTS(text=text, lang=lang, slow=False)
            
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
                tts.save(temp_file.name)
                
                with open(temp_file.name, 'rb') as f:
                    audio_bytes = f.read()
                
                os.unlink(temp_file.name)
                return audio_bytes
                
        except Exception as e:
            print(f"TTS error: {e}")
            return None
