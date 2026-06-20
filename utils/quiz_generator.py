import os
from openai import OpenAI
import streamlit as st
import json

class QuizGenerator:
    """Generate educational quizzes in Hinglish"""
    
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            st.error("⚠️ OpenAI API key not found. Please add it to .env file")
            self.client = None
        else:
            self.client = OpenAI(api_key=api_key)
        
        self.system_prompt = """You are a quiz generator for government school students in Haryana, India.

Your role:
- Create educational quizzes in simple Hinglish (Hindi + English mix)
- Use language suitable for students aged 10-16 years
- Questions should be clear and unambiguous
- Mix easy, medium, and hard questions
- Provide helpful explanations

Quiz format requirements:
- Generate exactly 5 multiple choice questions
- Each question has 4 options (A, B, C, D)
- Mark the correct answer
- Provide brief explanation for each answer
- Use Hinglish language (Roman script)

Content guidelines:
- Questions should test understanding, not just memory
- Use examples relevant to Indian context
- Avoid controversial or sensitive topics
- Keep language simple and clear
- Be encouraging in explanations

Output format (JSON):
{
  "topic": "topic name",
  "questions": [
    {
      "question": "Question text in Hinglish?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct": 0,
      "explanation": "Brief explanation in Hinglish"
    }
  ]
}"""
    
    def generate_quiz(self, topic, num_questions=5):
        """
        Generate a quiz on the given topic
        
        Args:
            topic: Topic for the quiz
            num_questions: Number of questions to generate (default 5)
        
        Returns:
            dict: Quiz data with questions, options, and answers
        """
        if not self.client:
            return self._get_fallback_quiz(topic)
        
        try:
            prompt = f"""Create a quiz on the topic: "{topic}"

Generate {num_questions} multiple choice questions in Hinglish.
Each question should have 4 options.
Output in JSON format as specified in your instructions."""

            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=1500
            )
            
            content = response.choices[0].message.content.strip()
            
            # Extract JSON from response
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].split("```")[0].strip()
            
            quiz_data = json.loads(content)
            
            # Validate quiz structure
            if "questions" not in quiz_data or len(quiz_data["questions"]) == 0:
                return self._get_fallback_quiz(topic)
            
            return quiz_data
            
        except Exception as e:
            st.error(f"Error generating quiz: {str(e)}")
            return self._get_fallback_quiz(topic)
    
    def _get_fallback_quiz(self, topic):
        """
        Return a fallback quiz when API fails
        """
        return {
            "topic": topic,
            "questions": [
                {
                    "question": f"{topic} ke baare mein ek basic question: Ye topic kyun important hai?",
                    "options": [
                        "Knowledge badhane ke liye",
                        "Sirf exam ke liye",
                        "Ye important nahi hai",
                        "Pata nahi"
                    ],
                    "correct": 0,
                    "explanation": "Knowledge badhana hamesa important hai. Ye humari samajh ko develop karta hai."
                },
                {
                    "question": f"{topic} ko seekhne ka best tareeka kya hai?",
                    "options": [
                        "Practice aur examples se",
                        "Sirf ratt ke",
                        "Ignore karna",
                        "Bas sunke"
                    ],
                    "correct": 0,
                    "explanation": "Practice aur real examples se hum concepts ko better samajh sakte hain."
                },
                {
                    "question": f"{topic} ka application real life mein kahan hota hai?",
                    "options": [
                        "Daily life situations mein",
                        "Kahin nahi",
                        "Sirf books mein",
                        "Sirf teachers ke liye"
                    ],
                    "correct": 0,
                    "explanation": "Har concept ka koi na koi practical application hota hai jo humari daily life mein useful hota hai."
                },
                {
                    "question": f"Agar {topic} samajh nahi aa raha to kya karna chahiye?",
                    "options": [
                        "Teacher se help lena aur practice karna",
                        "Chod dena",
                        "Guess karna",
                        "Tension lena"
                    ],
                    "correct": 0,
                    "explanation": "Help lena aur practice karna sabse best approach hai. Har student ki speed alag hoti hai."
                },
                {
                    "question": f"{topic} ko master karne mein kitna time lagta hai?",
                    "options": [
                        "Regular practice se kuch weeks mein",
                        "Ek din mein",
                        "Kabhi nahi ho sakta",
                        "Sirf genius log hi kar sakte hain"
                    ],
                    "correct": 0,
                    "explanation": "Regular practice aur dedication se koi bhi topic master kar sakta hai. Time har student ke liye alag hota hai."
                }
            ]
        }
    
    def validate_answer(self, question_data, user_answer):
        """
        Validate user's answer
        
        Args:
            question_data: Question dictionary with correct answer
            user_answer: User's answer (0-3 for A-D)
        
        Returns:
            dict: {
                'correct': bool,
                'explanation': str
            }
        """
        correct = question_data['correct']
        is_correct = (user_answer == correct)
        
        return {
            'correct': is_correct,
            'explanation': question_data.get('explanation', '')
        }
