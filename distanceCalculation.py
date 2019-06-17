from math import *
import numpy as np

def calculate_distance(iLat, iLon):
    #Dublin's location
    dlat = radians(53.339428)
    dlon = radians(-6.257664)

    lat = iLat
    lat = radians(lat)
    lon = iLon
    lon = radians(lon)

    x = sin(lat) * sin(dlat) + cos(lat) * cos(dlat) * cos(abs(dlon - lon))
    dist = acos(x)
    dist = 6371 * dist #convert to km
    return dist