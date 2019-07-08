import unittest
from implementation.coordinate import Coordinate


class TestCoordinate(unittest.TestCase):

    def setUp(self):
        self.coord = Coordinate(53.038056, -7.653889)

    def test_to_radians_valid(self):
        # verify if conversion of degrees to radians works
        test_coord1 = self.coord.to_radians()
        test_coord2 = Coordinate(0.9256887060571336, -0.13358556363217627)
        self.assertEqual(test_coord2.lat, test_coord1.lat)
        self.assertEqual(test_coord2.lon, test_coord1.lon)

    def test_to_radians_invalid(self):
        # verify if conversion of degrees to radians works
        test_coord1 = self.coord.to_radians()
        test_coord2 = Coordinate(75, -27)
        self.assertEqual(test_coord2.lat, test_coord1.lat)
        self.assertEqual(test_coord2.lon, test_coord1.lon)

    def test_substraction_valid(self):
        test_coord1 = Coordinate(52.038056, -7.653889)
        test_coord2 = Coordinate(1, 0)
        result_coord = self.coord - test_coord1
        self.assertEqual(test_coord2.lat, result_coord.lat)
        self.assertEqual(test_coord2.lon, result_coord.lon)

    def test_substraction_invalid(self):
        test_coord1 = Coordinate(52.038056, -7.653889)
        test_coord2 = Coordinate(0, 0)
        result_coord = self.coord - test_coord1
        self.assertEqual(test_coord2.lat, result_coord.lat)
        self.assertEqual(test_coord2.lon, result_coord.lon)


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
