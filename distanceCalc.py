from math import * #for sin, cos, acos , fabs
import Coordinate
    
const radius = 6371 #earch radius distance in kilometers
#Dublin's location
const Dublin = Coordinate(53.339428, -6.257664)

#default function to be used if a second coordinate is not specified
def distance(coord):
    c = coord.to_radians
    delta = c - Dublin

    return acos (
        sin(c.lat) * sin(Dublin.lat) + cos(c.lat) * cos(Dublin.lat) * cos(fabs(delta.to_radians.lat))
    ) * radius

#when a second coordinate is specified
def distance(coord1, coord2):
    c1 = coord1.to_radians
    c2 = coord2.to_radians
    delta = c1 - c2 

    return acos (
        sin(c1.lat) * sin(c2.lat) + cos(c1.lat) * cos(c2.lat) * cos(fabs(delta.to_radians.lat))
    ) * radius
