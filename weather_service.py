import os
import requests
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/"

def get_current_weather(city = "Wroclaw,PL"):
    response = requests.get(f"{BASE_URL}weather",
                 params={
                     "q": city,
                     "appid": API_KEY,
                     "units": "metric",
                     "lang": "pl"
                 })

    data = response.json()

    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "timestamp": datetime.now().isoformat()
    }

    #print(data)

# response = requests.get(f"{BASE_URL}forecast",
#              params={
#                  "q": "Wroclaw,PL",
#                  "appid": API_KEY,
#                  "units": "metric",
#                  "lang": "pl"
#              })
#
# data = response.json()

# print(data['list'][0]['dt_txt'], data['list'][0]['main']['temp'], "'C")

if __name__ == "__main__":
    print("=== TEST SERWISU POGODOWEGO ===")

    current = get_current_weather()
    print(f"Miasto:      {current["city"]}")
    print(f"Temperatura: {current["temperature"]}'C")
    print(f"Opis:        {current["description"]}")
