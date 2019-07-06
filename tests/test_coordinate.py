import unittest
from implementation.coordinate import Coordinate

class TestCoordinate(unittest.TestCase):

    def set_up(self):
        self.coord = Coordinate(53.038056, -7.653889)

    def test_to_radians(self):
        #verify if conversion of degrees to radians works
        test_coord1=self.coord.to_radians()
        test_coord2=Coordinate(0.9256887060571336,-0.13358556363217627)
        self.assertEqual(test_coord2, test_coord1)

    def test_substraction(self):
        test_coord1=Coordinate(52.038056, -7.653889)
        test_coord2=Coordinate(1,0)
        result_coord=self.coord-test_coord1
        self.assertEqual(test_coord2, result_coord)

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")