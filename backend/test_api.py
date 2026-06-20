#!/usr/bin/env python3
"""
Simple test script to verify backend is working
Run this before starting frontend
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_health():
    """Test if API is running"""
    print("🔍 Testing health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        if response.status_code == 200:
            print("✅ Backend is healthy!")
            print(f"   Response: {response.json()}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to backend. Is it running?")
        print("   Start it with: python app.py")
        return False

def test_explain():
    """Test explain endpoint"""
    print("\n🔍 Testing explain endpoint...")
    try:
        payload = {"question": "What is gravity?"}
        response = requests.post(f"{BASE_URL}/api/explain", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            if "explanation" in data:
                print("✅ Explain endpoint working!")
                print(f"   Question: {payload['question']}")
                print(f"   Answer: {data['explanation'][:100]}...")
                return True
            else:
                print(f"❌ Unexpected response: {data}")
                return False
        else:
            print(f"❌ Explain failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_quiz():
    """Test quiz generation endpoint"""
    print("\n🔍 Testing quiz endpoint...")
    try:
        payload = {"topic": "Mathematics", "num_questions": 3}
        response = requests.post(f"{BASE_URL}/api/quiz/generate", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            if "questions" in data and len(data["questions"]) > 0:
                print("✅ Quiz endpoint working!")
                print(f"   Topic: {data.get('topic', 'N/A')}")
                print(f"   Questions: {len(data['questions'])}")
                print(f"   First Q: {data['questions'][0]['question'][:60]}...")
                return True
            else:
                print(f"❌ Invalid quiz data: {data}")
                return False
        else:
            print(f"❌ Quiz generation failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("=" * 60)
    print("🧪 Backend API Test Suite")
    print("=" * 60)
    
    results = []
    
    # Test health
    results.append(("Health Check", test_health()))
    
    # Test explain (only if health check passed)
    if results[0][1]:
        results.append(("Explain API", test_explain()))
        results.append(("Quiz API", test_quiz()))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Test Summary")
    print("=" * 60)
    for test_name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name:20} : {status}")
    
    total = len(results)
    passed = sum(1 for _, p in results if p)
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Backend is ready.")
        print("   You can now start the frontend with: npm start")
    else:
        print("\n⚠️  Some tests failed. Check:")
        print("   1. Is backend running? (python app.py)")
        print("   2. Is GEMINI_API_KEY set in .env?")
        print("   3. Check backend logs for errors")

if __name__ == "__main__":
    main()
