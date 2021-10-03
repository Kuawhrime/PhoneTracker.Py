#download these librairy
#https://opencagedata.com/tutorials/geocode-in-python
#https://python-visualization.github.io/folium/quickstart.html
#https://pypi.org/project/phonenumbers/

import phonenumbers

import opencage

import folium

from myNumber import number
from opencage import geocoder
#geocoder is a way for geolocolisation
from phonenumbers import geocoder
key = "your opencage geocoder token"

samNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumber, "en")
print(yourLocation)

## get service operator
#carrier is somethings that goes tell you your mobile operator
from phonenumbers import carrier

service_operator = phonenumbers.parse(number)
print(carrier.name_for_number(service_operator, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourLocation)

results = geocoder.geocode(query)
print(results)

#latitude/longitude
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)

folium.Marker([lat, lng], popup = yourLocation).add_to((myMap))

# save map in html file

myMap.save("myLocation.html")
