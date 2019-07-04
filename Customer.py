from Coordinate import Coordinate

class Customer(object):

    def __init__(self, id=0, name='None', lat=0, lon=0):
        self.id=id
        self.name = name
        self.coord=Coordinate(lat, lon)

    def get_coord(self):
        return Coordinate(self.coord.lat, self.coord.lon)