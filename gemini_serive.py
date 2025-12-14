import json
from weather_service import get_forecast
from dotenv import load_dotenv
from google import genai
load_dotenv()


client = genai.Client()

def analize_forecast(forecast_data):
    prompt = f"""Przeanalizuj poniższą prognozę pogody i zwróć analizę.

    Dane prognozy:
    {forecast_data}

    Odpowiedz TYLKO w formacie JSON, bez żadnego dodatkowego tekstu:
    {{
      "city": "Warszawa",
      "period": "2024-01-15 - 2024-01-20",
      "temperature_trend": "spadkowy",
      "min_temp": -5.0,
      "max_temp": 8.0,
      "clothing_recommendation": "Ciepła kurtka, szalik, czapka",
      "warnings": ["Możliwe opady śniegu w dniu 2024-01-18"],
      "summary": "Tydzień z wyraźnym ochłodzeniem..."
    }}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )

    text = response.text
    if text.startswith("```json"):
        text = text.split("\n", 1)[1]
        text = text.split("```")[0]

    return json.loads(text)

if __name__ == "__main__":
    print("=== TEST SERWISU ANALIZY POGODY ===")
    analisys = analize_forecast(get_forecast())
    print(analisys)