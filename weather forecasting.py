import requests

def weather(api_key, city):
    weathermap_url = "https://api.openweathermap.org/data/2.5/weather?"
    params = {
       'q': city,
       'appid': api_key,
       'units': 'metric' 
            }
    try:
        response = requests.get(weathermap_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            print("\nCurrent weather condition in",city,"....\n")
            print(f'''Weather in {city} : {weather_description}
Temperature in (Celsius): {temperature}°C
Humidity in (Percent): {humidity} %
Pressure in (Hectopascal) : {pressure} hpa''')
        else:
            print(f"Error : {data['message']}")

    except Exception as e:
        print(f"An error occurred : {e}")

city = input("Enter the city name : ")
api_key = "a49de69b810181cc6659a996563a51dc"
weather(api_key, city)