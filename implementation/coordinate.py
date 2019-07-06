from math import radians # Just so I don't have to use math.radians(...)

class Coordinate(object):

    def __init__(self, lat=0, lon=0):
        self.lat=lat
        self.lon=lon

    def __sub__(self, other):
        return self.__class__(self.lat-other.lat, self.lon-other.lon)

    def to_radians(self):
        return  self.__class__(radians(self.lat), radians(self.lon))

    def __eq__(self, other):
        if self.lat==other.lat and self.lon==other.lon:
            return True
        else:
            return False    

    def __str__(self):
        return self.lat + " " + self.lon    