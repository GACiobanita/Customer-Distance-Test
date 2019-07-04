from math import radians # Just so I don't have to use math.radians(...)

class Coordinate(object):

    def __init__(self, lat=0, lon=0):
        self.lat=lat
        self.lon=lon

    def __sub__(self, other):
        return self.__class__(self.lat-other.lat, self.lon-other.lon)

    def to_radians(self):
        return  self.__class__(radians(self.lat), radians(self.lon))