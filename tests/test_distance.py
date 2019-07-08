import unittest
from implementation import distance_calc
from implementation.coordinate import Coordinate


class TestDistance(unittest.TestCase):

    def test_distance_dublin_valid(self):
        test_coord = Coordinate(52.986375, -6.043701)
        self.assertEqual(41.76872550078046, distance_calc.distance(test_coord))

    def test_distance_dublin_invalid(self):
        test_coord = Coordinate(62.986375, -2.043701)
        self.assertEqual(40.76872550078046, distance_calc.distance(test_coord))

    def test_distance_multiple_valid(self):
        test_coord1 = Coordinate(52.986375, -6.043701)
        test_coord2 = Coordinate(51.92893, -10.27699)
        self.assertEqual(309.9365659534358, distance_calc.distance(test_coord1, test_coord2))

    def test_distance_multiple_invalid(self):
        test_coord1 = Coordinate(53.986375, -6.043701)
        test_coord2 = Coordinate(56.92893, -10.27699)
        self.assertEqual(150.9365659534358, distance_calc.distance(test_coord1, test_coord2))


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
