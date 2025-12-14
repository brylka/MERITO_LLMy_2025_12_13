import os
import requests
from dotenv import load_dotenv
from google import genai
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/"

# response = requests.get(f"{BASE_URL}weather",
#              params={
#                  "q": "Wroclaw,PL",
#                  "appid": API_KEY,
#                  "units": "metric",
#                  "lang": "pl"
#              })
#
# data = response.json()

# print(data)

response = requests.get(f"{BASE_URL}forecast",
             params={
                 "q": "Wroclaw,PL",
                 "appid": API_KEY,
                 "units": "metric",
                 "lang": "pl"
             })

data = response.json()

# print(data['list'][0]['dt_txt'], data['list'][0]['main']['temp'], "'C")




client = genai.Client()


prompt = f"""Przeanalizuj poniższą prognozę pogody i zwróć analizę.

Dane prognozy:
{data}

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

print(f"Gemini: {response.text}")