import unittest
from Coordinate import Coordinate

class TestCoordinate(unittest.TestCase):

    def setUp(self):
        self.coord = Coordinate(53.038056, -7.653889)

    def test_to_radians(self):
        #verify if conversion of degrees to radians works
        testCoord=self.coord.to_radians()
        self.assertEqual(0.9256887060571336, testCoord.lat)
        self.assertEqual(-0.13358556363217627, testCoord.lon)

    def test_substraction(self):
        testCoord=Coordinate(52.038056, -7.653889)
        resultCoord=self.coord-testCoord
        self.assertEqual(1, resultCoord.lat)
        self.assertEqual(0, resultCoord.lon)

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")