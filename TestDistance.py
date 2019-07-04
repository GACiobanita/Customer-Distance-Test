import unittest
import distanceCalc
from Coordinate import Coordinate

class TestDistance(unittest.TestCase):

    def test_distance1(self):
        testCoord=Coordinate(52.986375,-6.043701)
        self.assertEqual(41.77, distanceCalc.distance(testCoord))

    def test_distance2(self):
        testCoord1=Coordinate(52.986375, -6.043701)
        testCoord2=Coordinate(51.92893, -10.27699)
        self.assertEqual(309.94, distanceCalc.distance(testCoord1, testCoord2))

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")