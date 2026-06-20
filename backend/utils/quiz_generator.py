import os
import google.generativeai as genai
import json

class QuizGenerator:
    """Generate quizzes using Google Gemini"""
    
    SYSTEM_PROMPT = """You are a quiz generator for Haryana government school students (grades 6-10).

CRITICAL RULES:
- ALL questions MUST be DIRECTLY related to the specific topic provided
- NO generic questions about "learning methods" or "importance of studying"
- Ask ONLY about actual content, concepts, facts and principles of the topic
- Write EVERY question in BOTH English AND Hindi (Devanagari)
- Write EVERY option in BOTH English AND Hindi (Devanagari)
- Write EVERY explanation in BOTH English AND Hindi (Devanagari)
- Generate exactly 5 multiple choice questions
- Each question has 4 options (A, B, C, D)
- Mix easy, medium, and hard difficulty
- All options should be plausible (not obviously wrong)
- Use Indian context examples when possible
- Output ONLY valid JSON, no markdown

BILINGUAL FORMAT FOR EACH FIELD:
- question: "English question? | हिंदी प्रश्न?"
- options: ["English A | हिंदी A", "English B | हिंदी B", ...]
- explanation: "English explanation. | हिंदी स्पष्टीकरण।"

JSON FORMAT:
{
  "topic": "topic name",
  "questions": [
    {
      "question": "What gas do plants release during photosynthesis? | प्रकाश संश्लेषण में पौधे कौन सी गैस छोड़ते हैं?",
      "options": [
        "Oxygen | ऑक्सीजन",
        "Carbon Dioxide | कार्बन डाइऑक्साइड",
        "Nitrogen | नाइट्रोजन",
        "Hydrogen | हाइड्रोजन"
      ],
      "correct": 0,
      "explanation": "Plants release oxygen during photosynthesis. | पौधे प्रकाश संश्लेषण के दौरान ऑक्सीजन छोड़ते हैं।"
    }
  ]
}
"""
    
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            self.model = None
        else:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel(
                model_name="gemini-2.5-flash",
                system_instruction=self.SYSTEM_PROMPT
            )
    
    def generate_quiz(self, topic: str, num_questions: int = 5) -> dict:
        """Generate a quiz on the given topic"""
        if not self.model:
            return self._get_fallback_quiz(topic)
        
        try:
            # Enhanced prompt to ensure topic-specific questions
            prompt = f"""Create a {num_questions} question quiz STRICTLY about: "{topic}"

IMPORTANT:
- Every question MUST test knowledge about {topic} specifically
- Write EVERY question, option, and explanation in BOTH English AND Hindi
- Format: "English text | हिंदी पाठ"
- NO generic questions about learning or studying
- Focus on actual content of {topic}

Generate the quiz now in JSON format."""

            response = self.model.generate_content(prompt)
            
            # Parse the response text
            response_text = response.text.strip()
            
            # Remove markdown code blocks if present
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0].strip()
            
            quiz_data = json.loads(response_text)
            
            # Validate structure
            if "questions" not in quiz_data or len(quiz_data["questions"]) == 0:
                return self._get_fallback_quiz(topic)
            
            # Ensure topic is set
            if "topic" not in quiz_data:
                quiz_data["topic"] = topic
            
            return quiz_data
            
        except Exception as e:
            print(f"Quiz generation error: {e}")
            return self._get_fallback_quiz(topic)
    
    def _get_fallback_quiz(self, topic: str) -> dict:
        """Fallback quiz when API fails - shows message to retry"""
        return {
            "topic": topic,
            "questions": [
                {
                    "question": f"Sorry! Quiz generation failed for '{topic}'. Please try again or choose a different topic.",
                    "options": [
                        "Click 'New Topic' to try again",
                        "Check your internet connection",
                        "Make sure API key is configured",
                        "Try a simpler topic name"
                    ],
                    "correct": 0,
                    "explanation": f"Unable to generate quiz for {topic}. API error or connection issue. Kripya phir se try karo!"
                }
            ]
        }
