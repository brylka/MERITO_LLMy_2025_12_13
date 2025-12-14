import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/"

response = requests.get(f"{BASE_URL}weather",
             params={
                 "q": "Wroclaw,PL",
                 "appid": API_KEY,
                 "units": "metric",
                 "lang": "pl"
             })

data = response.json()

# print(data)

response = requests.get(f"{BASE_URL}forecast",
             params={
                 "q": "Wroclaw,PL",
                 "appid": API_KEY,
                 "units": "metric",
                 "lang": "pl"
             })

data = response.json()

print(data['list'][0]['dt_txt'], data['list'][0]['main']['temp'], "'C")
