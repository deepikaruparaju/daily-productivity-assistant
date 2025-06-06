import requests

API_KEY = "2909fb0e6e7e830543aa4ac998edd7d5"  # 🔑 Replace with your OpenWeatherMap API key

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            return f"Weather error: {data.get('message', 'Unknown error')}"
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        return f"🌤️ Weather in {city.title()}:\n- {weather}\n- Temp: {temp}°C\n- Feels Like: {feels_like}°C"
    except Exception as e:
        return f"Error fetching weather: {e}"
