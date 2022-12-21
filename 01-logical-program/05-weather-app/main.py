import requests

API_KEY = "36209f4e7d834a39a3a132128222112"

def print_weather_data(city):
    url = "https://api.weatherapi.com/v1/current.json?key="+API_KEY+"&q="+city+"&aqi=no"
    res = requests.get(url)
    data = res.json()
    temperature_in_celsius = data["current"]["temp_c"]
    temperature_in_fahrenheit = data["current"]["temp_f"]
    wind_kph = data["current"]["wind_kph"]
    humidity = data["current"]["humidity"]
    print(f"City                      : {city}")
    print(f"Temperature in celsius    : {temperature_in_celsius}")
    print(f"Temperature in fahrenheit : {temperature_in_fahrenheit}")
    print(f"Wind speed in kph         : {wind_kph}")
    print(f"Humidity in %             : {humidity}")


def main():
    city = getUserInput('Enter the city: ')
    if city == 1:

    elif choice == 2:
        ...
        n -= 1
    elif choice == 3:
        ...
        n -= 1
    else:
        print 'Please choose the correct city name'
    
    print_weather_data(city)



if __name__=='__main__':
        main()