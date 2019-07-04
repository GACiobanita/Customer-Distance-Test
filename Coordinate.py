from math import radians # Just so I don't have to use math.radians(...)

class Coordinate:
    def __init__(self, lat, lon):
        self.lat=lat
        self.long=lon

    def __sub__(self, other):
        return self.__class__(self.lat-other.lat, self.lon-other.lon)

    def to_radians():
        return  self.__class__(radians(self.lat), radians(self.lon))