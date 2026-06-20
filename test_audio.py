#!/usr/bin/env python3
"""
Test script to check if microphone and audio are working correctly
"""

import speech_recognition as sr
from gtts import gTTS
import os
import tempfile

def test_microphone():
    """Test if microphone is working"""
    print("Testing microphone...")
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            print("✓ Microphone detected")
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=2)
            print("✓ Noise adjustment complete")
            
            print("\nPlease speak something (you have 5 seconds)...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("✓ Audio captured")
            
            # Try to recognize
            print("Converting speech to text...")
            text = recognizer.recognize_google(audio, language="en-IN")
            print(f"✓ Recognized: '{text}'")
            
            return True
            
    except sr.WaitTimeoutError:
        print("✗ No speech detected")
        return False
    except sr.UnknownValueError:
        print("✗ Could not understand audio")
        return False
    except sr.RequestError as e:
        print(f"✗ API error: {e}")
        return False
    except OSError as e:
        print(f"✗ Microphone error: {e}")
        print("  Make sure microphone is connected and permissions are granted")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_speakers():
    """Test if speakers/audio output is working"""
    print("\nTesting speakers...")
    
    try:
        # Create test speech
        text = "Testing audio output. If you can hear this, speakers are working."
        tts = gTTS(text=text, lang='en', slow=False)
        
        # Save to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            temp_file = fp.name
            tts.save(temp_file)
        
        print("✓ Audio file created")
        print(f"Playing audio from: {temp_file}")
        print("You should hear a test message...")
        
        # Try to play (platform-specific)
        if os.name == 'nt':  # Windows
            os.system(f'start {temp_file}')
        elif os.name == 'posix':  # Linux/Mac
            os.system(f'afplay {temp_file}' if os.uname().sysname == 'Darwin' else f'mpg123 {temp_file}')
        
        input("Did you hear the test message? (Press Enter)")
        
        # Cleanup
        try:
            os.remove(temp_file)
        except:
            pass
        
        print("✓ Speaker test complete")
        return True
        
    except Exception as e:
        print(f"✗ Speaker error: {e}")
        return False

def list_microphones():
    """List all available microphones"""
    print("\nAvailable microphones:")
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"  [{index}] {name}")

if __name__ == "__main__":
    print("=" * 60)
    print("Audio System Test for Voice-Enabled AI Teaching Assistant")
    print("=" * 60)
    
    # List available microphones
    try:
        list_microphones()
    except Exception as e:
        print(f"Could not list microphones: {e}")
    
    print("\n" + "=" * 60)
    
    # Test microphone
    mic_result = test_microphone()
    
    # Test speakers
    speaker_result = test_speakers()
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary:")
    print(f"  Microphone: {'✓ PASSED' if mic_result else '✗ FAILED'}")
    print(f"  Speakers:   {'✓ PASSED' if speaker_result else '✗ FAILED'}")
    print("=" * 60)
    
    if mic_result and speaker_result:
        print("\n✓ All tests passed! You can run the application.")
    else:
        print("\n✗ Some tests failed. Please check:")
        if not mic_result:
            print("  - Microphone is connected")
            print("  - Microphone permissions are granted")
            print("  - No other application is using the microphone")
        if not speaker_result:
            print("  - Speakers/headphones are connected")
            print("  - Volume is turned up")
            print("  - Audio drivers are installed")
            