import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  # You can change the units to imperial if you prefer Fahrenheit

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"Weather forecast in {city}:")
            print(f"Temperature in {city}: {data['main']['temp']}°C")
            print(f"Description: {data['weather'][0]['description']}")
            print(f"Humidity in {city}: {data['main']['humidity']}%")
            print(f"Wind Speed in {city}: {data['wind']['speed']} m/s")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    api_key = "e7b5099e5f6abd30c205894ceebdf8f1"
    city = input("Enter the name of the city: ")
    get_weather(api_key, city)