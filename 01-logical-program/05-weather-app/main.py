import requests

API_KEY = "36209f4e7d834a39a3a13212822211"

def print_weather_data(city):
    url = "https://api.weatherapi.com/v1/current.json?key="+API_KEY+"&q="+city+"&aqi=no"
    response = requests.get(url)
    data = response.json()
    choosed_city = data["location"]["name"]
    temperature_in_celsius = data["current"]["temp_c"]
    temperature_in_fahrenheit = data["current"]["temp_f"]
    wind_kph = data["current"]["wind_kph"]
    humidity = data["current"]["humidity"]
    print(f"\nCity                      : {choosed_city}")
    print(f"Temperature in celsius    : {temperature_in_celsius}")
    print(f"Temperature in fahrenheit : {temperature_in_fahrenheit}")
    print(f"Wind speed in kph         : {wind_kph}")
    print(f"Humidity in %             : {humidity}")


def main():
    print("Weather app to give the temperature, wind speed and humidity details \n")
    print("1 - Kanyakumari")
    print("2 - Tirunelveli")
    print("3 - Madurai")
    print("4 - Chennai")
    print("5 - Delhi\n")

    while True:
        choice = int(input('Choose the city from above list : '))
        if choice == 1:
            print_weather_data("kanyakumari")
            break
        elif choice == 2:
            print_weather_data("tirunelveli")
            break
        elif choice == 3:
            print_weather_data("madurai")
            break
        elif choice == 4:
            print_weather_data("chennai")
            break
        elif choice == 5:
            print_weather_data("delhi")
            break
        else:
            print("\nPlease choose the correct city from the above list")


if __name__=='__main__':
    main()
