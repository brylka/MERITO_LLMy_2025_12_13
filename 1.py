from google import genai
from dotenv import load_dotenv
load_dotenv()

client = genai.Client()
history = []
history.append({"role": "model", "parts": [{"text": "Odpowiadaj zawsze po angielsku - nawet jak będzie pytanie po polsku."}]})

while True:
    message = input("Ja: ")
    history.append({"role": "user", "parts": [{"text": message}]})
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=history
    )
    history.append({"role": "model", "parts": [{"text": response.text}]})
    print(f"Gemini: {response.text}")