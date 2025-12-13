from google import genai
from dotenv import load_dotenv
load_dotenv()

client = genai.Client()

task = input("Zadanie (np. 2+2): ")
answer = input("Twoja odpowiedź: ")

prompt = f"""Sprawdź czy odpowiedź na zadanie jest poprawna.
Zadanie: {task}
Odpowiedź użytkownika: {answer}

Odpowiedz TYLKO w formacie JSON, bez żadnego dodatkowego tekstu:
{{"is_correct": true/false, "result": poprawny_wynik}}"""

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=prompt
)

text = response.text
if text.startswith("```"):
    text = text.split("\n", 1)[1]
print(f"Gemini: {text}")