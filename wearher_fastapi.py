from fastapi import FastAPI
from weather_service import get_current_weather, get_forecast

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Witaj Świecie!"}

@app.get("/weather/current")
def current_weather():
    return get_current_weather()

@app.get("/weather/forecast")
def forecast_weather():
    return get_forecast()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)