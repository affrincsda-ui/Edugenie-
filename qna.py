
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = os.getenv(
    "GEMINI_MODEL", "gemini-2.5-flash"
)

def answer_question(question):
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=f"""
            You are EduGenie, an educational assistant.
            Answer the following question in simple,
            student-friendly language.

            Question: {question}
            """
        )
        return response.text

    except Exception as e:
        return f"Error generating answer: {e}"
      
