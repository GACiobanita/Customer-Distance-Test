from math import * #for sin, cos, acos , fabs, radians
from . import Coordinate
    
#Dublin's location
DUBLIN = Coordinate(radians(53.339428), radians(-6.257664))
RADIUS = 6371 #earch radius distance in kilometers

#default function to be used if a second coordinate is not specified

#when a second coordinate is specified
def distance(coord1, coord2=None):

    if coord2 is None:
        c = coord1.to_radians()
        delta = c - DUBLIN

        return acos (
            sin(c.lat) * sin(DUBLIN.lat) + cos(c.lat) * cos(DUBLIN.lat) * cos(fabs(delta.lon))
        ) * RADIUS
    else:
        c1 = coord1.to_radians()
        c2 = coord2.to_radians()
        delta = c1 - c2 

        return acos (
            sin(c1.lat) * sin(c2.lat) + cos(c1.lat) * cos(c2.lat) * cos(fabs(delta.lon))
        ) * RADIUS
