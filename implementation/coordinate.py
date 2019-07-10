from math import radians  # Just so I don't have to use math.radians(...)


# The Coordinate class allows us to store latitude(lat) and longitude(lon) from the .txt file
# I've created operation functions for use between variables of the Coordinate class

class Coordinate(object):

    def __init__(self, lat=0, lon=0):
        self.lat = lat
        self.lon = lon

    # If there is no __sub__ override then Python would have thrown an Exception error
    def __sub__(self, other):
        return self.__class__(self.lat - other.lat, self.lon - other.lon)

    def to_radians(self):
        return self.__class__(radians(self.lat), radians(self.lon))

    # If there is no __eq__ override then Python would have always considered variables of class Coordinate to be equal
    # as Python would have compared them only at the level of variable type
    def __eq__(self, other):
        if self.lat == other.lat and self.lon == other.lon:
            return True
        else:
            return False

    def __str__(self):
        return str(self.lat) + " " + str(self.lon)
