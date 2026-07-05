import requests

api_key = "0b453823dabaaa058e61ca5cb4c8c4af"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"


def fetch_data():
    print("Fetching data from the Weather API...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("API request successful!")
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None


def mock_fetch_data():
    print("Mock fetching data from the Weather API...")
    mock_response = {
        "request": {
            "type": "City",
            "query": "New York, United States of America",
            "language": "en",
            "unit": "m"
        },
        "location": {
            "name": "New York",
            "country": "United States of America",
            "region": "New York",
            "lat": "40.714",
            "lon": "-74.006",
            "timezone_id": "America/New_York",
            "localtime": "2024-06-01 12:00",
            "localtime_epoch": 1712102400,
            "utc_offset": "-4.0"
        },
        "current": {
            "temperature": 25,
            "weather_descriptions": ["Partly cloudy"],
            "wind_speed": 10,
            "humidity": 60
        }
    }
    print("Mock API request successful!")
    return mock_response