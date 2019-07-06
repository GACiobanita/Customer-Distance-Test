import unittest
from implementation import distanceCalc
from implementation.coordinate import Coordinate

class TestDistance(unittest.TestCase):

    def test_distance1(self):
        test_coord=Coordinate(52.986375,-6.043701)
        self.assertEqual(41.76872550078046, distanceCalc.distance(test_coord))

    def test_distance2(self):
        test_coord1=Coordinate(52.986375, -6.043701)
        test_coord2=Coordinate(51.92893, -10.27699)
        self.assertEqual(309.9365659534358, distanceCalc.distance(test_coord1, test_coord2))

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")