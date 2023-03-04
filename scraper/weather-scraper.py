from functools import partial
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="MyApp")

print("     Weather Scraper\n" + 
        "-------------------------\n" + 
        "Zack Martin, Sheel Patel\n" +
        "To Exit: 'E' or 'e'")

while True:
    inp = (input("\nSearch for: ")).lower()

    if inp == 'e':
        break 

    try:   
        coords = geolocator.geocode(inp)
        latitude = str(round(coords.latitude,2))
        longitude = str(round(coords.longitude,2))

        geocode = partial(geolocator.geocode, language="en")
        address = str(geocode(inp))
        address = address.split(", ")
        city = address[0]
        state = address[len(address) - 2]

        url = f"https://weather.com/weather/today/l/{latitude},{longitude}?par=google"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        currTemp = soup.find(class_="CurrentConditions--tempValue--MHmYY").text
        feelsLike = soup.find(class_="CurrentConditions--phraseValue--mZC_p").text
        highLow = soup.find(class_="WeatherDetailsListItem--wxData--kK35q").text
        wind = soup.find(class_="Wind--windWrapper--3Ly7c undefined").text.removeprefix("Wind Direction")

        titleLine = city + ", " + state + " (" + latitude + ", " + longitude + ")"
        print("\n" + titleLine)
        print("-" * len(titleLine))
        print("Temp:    " + currTemp) 
        print("Current: " + feelsLike)
        print("H/L:     " + highLow)
        print("Wind:    " + wind + "")

    except:
        print("\nInvalid location")