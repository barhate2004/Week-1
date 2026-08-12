import requests

API_KEY = "bd5e378503939ddaee76f12ad7a97608"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()

            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]

            print("\n==============================")
            print("       WEATHER INFORMATION")
            print("==============================")
            print(f"City:        {data['name']}")
            print(f"Temperature: {temperature}°C")
            print(f"Feels Like:  {feels_like}°C")
            print(f"Humidity:    {humidity}%")
            print(f"Description: {description.capitalize()}")
            print("==============================")

        elif response.status_code == 401:
            print("\nError: Invalid or inactive API key.")
            print("Please check your OpenWeather API key.")

        elif response.status_code == 404:
            print("\nError: City not found.")
            print("Please enter a valid city name.")

        elif response.status_code == 429:
            print("\nError: API request limit exceeded.")

        else:
            print(f"\nUnable to fetch weather data.")
            print(f"Status code: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("\nError: Could not connect to the weather service.")

    except requests.exceptions.Timeout:
        print("\nError: Request timed out.")

    except requests.exceptions.RequestException as e:
        print(f"\nError: {e}")


def main():
    print("==============================")
    print("       WEATHER CLI APP")
    print("==============================")

    city = input("Enter city name: ").strip()

    if city:
        get_weather(city)
    else:
        print("Please enter a city name.")


if __name__ == "__main__":
    main()