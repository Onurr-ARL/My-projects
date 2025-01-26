import requests

# This script fetches current weather data for a city using the OpenWeatherMap API.
# How to use:
# - Replace `your_api_key_here` with your OpenWeatherMap API key.
# - Run the script, enter the city name when prompted, and see the weather data.

def get_weather_data(city, api_key):
    """
    Fetches current weather data for a given city using OpenWeatherMap API.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"Weather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Condition: {data['weather'][0]['description'].capitalize()}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except KeyError:
        print("City not found or invalid API key.")

# Example usage
if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    get_weather_data(city_name, api_key)