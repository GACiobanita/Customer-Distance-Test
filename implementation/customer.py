from .coordinate import Coordinate


# how information from the customer.txt file will be stored during program activity
class Customer(object):

    def __init__(self, id=0, name='None', lat=0, lon=0):
        self.id = id
        self.name = name
        self.coord = Coordinate(lat, lon)

    def get_coord(self):
        return Coordinate(self.coord.lat, self.coord.lon)

    def __eq__(self, other):
        if (self.id == other.id and
                self.name == other.name and
                self.coord == other.coord):
            return True
        else:
            return False

    def __str__(self):
        return "Customer " + self.name + " with ID: " + self.id + " and coordinates: " + self.coord
