#!/usr/bin/env python3
"""
Test Gemini API connection
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

print("=" * 70)
print("🧪 Testing Gemini API Connection")
print("=" * 70)

# Check API key
api_key = os.getenv("GEMINI_API_KEY")
print(f"\n1. API Key Check:")
if not api_key:
    print("   ❌ No API key found in .env file")
    print("   👉 Add GEMINI_API_KEY to backend/.env")
    exit(1)
else:
    print(f"   ✅ API key found: {api_key[:10]}...{api_key[-5:]}")
    print(f"   Key length: {len(api_key)} characters")

# Configure Gemini
print(f"\n2. Configuring Gemini API...")
try:
    genai.configure(api_key=api_key)
    print("   ✅ Configuration successful")
except Exception as e:
    print(f"   ❌ Configuration failed: {e}")
    exit(1)

# List available models
print(f"\n3. Listing available models...")
try:
    models = genai.list_models()
    print("   ✅ Available models:")
    for model in models:
        if 'generateContent' in model.supported_generation_methods:
            print(f"      • {model.name}")
except Exception as e:
    print(f"   ❌ Failed to list models: {e}")
    print("\n   Possible issues:")
    print("   • API key is invalid or expired")
    print("   • Need to create key from: https://aistudio.google.com/app/apikey")
    exit(1)

# Test with gemini-2.5-flash
print(f"\n4. Testing gemini-2.5-flash model...")
try:
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content("Say hello in one word")
    print(f"   ✅ Model works!")
    print(f"   Response: {response.text}")
except Exception as e:
    print(f"   ❌ Model test failed: {e}")
    exit(1)

# Test quiz generation
print(f"\n5. Testing quiz generation...")
try:
    system_prompt = """Generate a simple quiz question about fractions in JSON format:
{"question": "What is 1/2 + 1/4?", "options": ["3/4", "1/6", "2/4", "3/8"], "correct": 0}"""
    
    model = genai.GenerativeModel(
        'gemini-pro',
        system_instruction=system_prompt
    )
    response = model.generate_content("Create one question about fractions")
    print(f"   ✅ Quiz generation works!")
    print(f"   Response: {response.text[:100]}...")
except Exception as e:
    print(f"   ❌ Quiz generation failed: {e}")
    exit(1)

print("\n" + "=" * 70)
print("🎉 All tests passed! Gemini API is working correctly!")
print("=" * 70)
print("\nYou can now use the app. Restart the backend:")
print("   cd backend")
print("   python app.py")
