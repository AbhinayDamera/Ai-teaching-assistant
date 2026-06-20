import os
import google.generativeai as genai
import streamlit as st


class AITeacher:
    """AI-powered teacher using Gemini — explains concepts in Hinglish."""

    SYSTEM_PROMPT = """You are an AI teaching assistant for government school students in Haryana, India (grades 6–10).

RULES:
- Always respond in Hinglish (natural mix of Hindi + English, Roman script only — no Devanagari).
- Keep sentences short, simple, and encouraging.
- Use real-life Indian examples (fields, markets, cricket, festivals).
- Structure every explanation like this:
  1. One-line simple answer
  2. Easy explanation with an example
  3. One fun fact or memory tip
- Never exceed 150 words per explanation.
- Stay strictly educational. Politely decline off-topic requests.

EXAMPLE:
Q: "Photosynthesis kya hai?"
A: "🌿 Simple jawab: Plants sunlight se apna khana banate hain!

Samjho aise — jaise hum roti banane ke liye aag use karte hain, waise plants sunlight use karte hain. Wo pani + CO2 + sunlight le kar glucose (meetha khana) banate hain aur oxygen chhodte hain.

💡 Yaad rakhne ki trick: Photo = Light, Synthesis = Banana. 'Sunlight se banana' — bas itna yaad rakho!"
"""

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            self.model = None
        else:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                system_instruction=self.SYSTEM_PROMPT,
            )

    def explain_concept(self, question: str) -> dict:
        """
        Returns {"explanation": str, "error": bool}
        """
        if not self.model:
            return {
                "explanation": "⚠️ Gemini API key nahi mili. .env file mein GEMINI_API_KEY add karo.",
                "error": True,
            }
        try:
            response = self.model.generate_content(question)
            return {"explanation": response.text.strip(), "error": False}
        except Exception as e:
            return {
                "explanation": f"❌ AI se response nahi aaya: {e}",
                "error": True,
            }
