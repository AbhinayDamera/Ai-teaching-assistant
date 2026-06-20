import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
import streamlit as st
from io import BytesIO

class VoiceHandler:
    """Handles speech-to-text and text-to-speech operations"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 4000
        self.recognizer.dynamic_energy_threshold = True
        
    def listen(self, language="hi-IN", timeout=5):
        """
        Listen to microphone input and convert to text
        
        Args:
            language: Language code for speech recognition (hi-IN for Hindi, en-IN for Indian English)
            timeout: Maximum time to wait for speech
        
        Returns:
            str: Recognized text or None if failed
        """
        try:
            with sr.Microphone() as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                # Listen for audio
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=10)
                
                # Try to recognize speech with multiple language options
                try:
                    # First try Hindi
                    text = self.recognizer.recognize_google(audio, language="hi-IN")
                    return text
                except sr.UnknownValueError:
                    # If Hindi fails, try English
                    try:
                        text = self.recognizer.recognize_google(audio, language="en-IN")
                        return text
                    except:
                        return None
                except sr.RequestError as e:
                    st.error(f"Could not request results; {e}")
                    return None
                    
        except sr.WaitTimeoutError:
            st.warning("No speech detected. Please try again.")
            return None
        except Exception as e:
            st.error(f"Error in speech recognition: {str(e)}")
            return None
    
    def speak(self, text, lang='hi'):
        """
        Convert text to speech and play it
        
        Args:
            text: Text to convert to speech
            lang: Language code ('hi' for Hindi, 'en' for English)
        """
        try:
            # Create gTTS object
            tts = gTTS(text=text, lang=lang, slow=False)
            
            # Save to temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
                temp_file = fp.name
                tts.save(temp_file)
            
            # Play audio using Streamlit
            with open(temp_file, 'rb') as audio_file:
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format='audio/mp3', autoplay=True)
            
            # Clean up
            try:
                os.remove(temp_file)
            except:
                pass
                
        except Exception as e:
            st.error(f"Error in text-to-speech: {str(e)}")
    
    def speak_hinglish(self, text):
        """
        Speak text in Hinglish (mixed Hindi-English)
        Automatically detects and uses appropriate language
        """
        # For Hinglish, we'll use Hindi TTS as it handles Roman Hindi better
        self.speak(text, lang='hi')
