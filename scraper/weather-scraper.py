import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="MyApp")

try:   
    input = input("Search for: ")

    location = geolocator.geocode(input)
    latitude = str(round(location.latitude,2))
    longitude = str(round(location.longitude,2))

    url = f"https://weather.com/weather/today/l/{latitude},{longitude}?par=google"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    currTemp = soup.find(class_="CurrentConditions--tempValue--MHmYY").text
    feelsLike = soup.find(class_="CurrentConditions--phraseValue--mZC_p").text
    highLow = soup.find(class_="WeatherDetailsListItem--wxData--kK35q").text
    wind = str(soup.find(class_="Wind--windWrapper--3Ly7c undefined").text).removeprefix("Wind Direction")

    print(latitude + ", " + longitude)
    print(currTemp) 
    print(feelsLike)
    print(highLow)
    print(wind)
except:
    print("Invalid location")