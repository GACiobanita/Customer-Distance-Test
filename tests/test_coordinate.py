import unittest
from implementation.coordinate import Coordinate

class TestCoordinate(unittest.TestCase):

    def setUp(self):
        self.coord = Coordinate(53.038056, -7.653889)

    def test_to_radians(self):
        #verify if conversion of degrees to radians works
        testCoord1=self.coord.to_radians()
        testCoord2=Coordinate(0.9256887060571336,-0.13358556363217627)
        self.assertEqual(testCoord2, testCoord1)

    def test_substraction(self):
        testCoord1=Coordinate(52.038056, -7.653889)
        testCoord2=Coordinate(1,0)
        resultCoord=self.coord-testCoord1
        self.assertEqual(testCoord2, resultCoord)

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")