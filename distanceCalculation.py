from math import *
import numpy as np

print("Input latitude and longitude to find the distance from Dublin(Lat:53.339428, Long:-6.257664)")
dlat = radians(53.339428)
dlon = radians(-6.257664)

try:
    flat =input('Enter latitude:')
    lat = float(flat)
    lat = radians(lat)
    flong = input('Enter longitude:')
    lon = float(flong)
    lon = radians(lon)
except:
    print('We need numbers for the formula to work.')

x = sin(lat) * sin(dlat) + cos(lat) * cos(dlat) * cos(abs(dlon - lon))
dist = acos(x)
dist = 6371 * dist #convert to km
print("The distance between Dublin and the input latitude and longitude is:", dist)