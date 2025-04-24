import requests

def get_weather(city: str) -> str:
    """Fetches the current weather for a specified city using Open-Meteo API (No API Key Needed).
    Args:
        city: The name of the city.
    """
    try:
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        geo_response = requests.get(geo_url)
        
        if geo_response.status_code == 200 and geo_response.json().get("results"):
            city_data = geo_response.json()["results"][0]
            lat, lon = city_data["latitude"], city_data["longitude"]
        else:
            return f"Error: Unable to find location for '{city}'."

        # Fetch weather data
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_response = requests.get(weather_url)

        if weather_response.status_code == 200:
            weather_data = weather_response.json()["current_weather"]
            temp = weather_data["temperature"]
            wind_speed = weather_data["windspeed"]
            
            return f"""Weather in {city}:
            Temperature: {temp}°C
            Wind Speed: {wind_speed} m/s"""
        else:
            return "Error fetching weather data."

    except Exception as e:
        return f"Error: {str(e)}"


print(get_weather("Torreon"))