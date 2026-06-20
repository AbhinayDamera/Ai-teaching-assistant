#!/usr/bin/env python3
"""
Test script to verify quiz questions are topic-specific
"""

import os
import sys
from dotenv import load_dotenv

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()

from utils.quiz_generator import QuizGenerator

def test_quiz_quality():
    """Test if quiz questions are topic-specific"""
    
    print("=" * 70)
    print("🧪 Testing Quiz Quality - Topic Relevance Check")
    print("=" * 70)
    
    generator = QuizGenerator()
    
    if not generator.model:
        print("❌ Gemini API not configured. Add GEMINI_API_KEY to .env file")
        return
    
    # Test topics
    test_topics = [
        "Photosynthesis",
        "Fractions",
        "Solar System",
        "Water Cycle"
    ]
    
    for topic in test_topics:
        print(f"\n📚 Generating quiz for: {topic}")
        print("-" * 70)
        
        quiz = generator.generate_quiz(topic, num_questions=3)
        
        if "questions" in quiz and len(quiz["questions"]) > 0:
            print(f"✅ Generated {len(quiz['questions'])} questions\n")
            
            for i, q in enumerate(quiz["questions"], 1):
                print(f"Q{i}: {q['question']}")
                
                # Check if question contains generic words
                generic_words = ["seekhna", "practice", "important", "kyun zaroori", 
                               "real life", "master banne", "difficult lag raha"]
                
                is_generic = any(word in q['question'].lower() for word in generic_words)
                
                if is_generic:
                    print("   ⚠️  WARNING: This seems like a generic question!")
                else:
                    print("   ✅ Topic-specific question")
                
                print(f"   Options: {', '.join(q['options'][:2])}...")
                print()
        else:
            print("❌ Failed to generate quiz")
    
    print("=" * 70)
    print("\n💡 TIP: All questions should be about the topic's content,")
    print("   not about how to study or why it's important!")
    print("\n✅ If you see topic-specific questions, the fix worked!")

if __name__ == "__main__":
    test_quiz_quality()
