import unittest
from implementation.organizer import Organizer

class TestOrganizer(unittest.TestCase):

    def setUp(self):
        self.organizer = Organizer()

    def test_acquire_filepath_valid(self):
        self.organizer.acquire_filepath()
        self.organizer.read_from_filepath()
        self.assertIsNot(0, len(self.organizer.fileData))

    def test_acquire_filepath_invalid(self):
        self.organizer.acquire_filepath()
        self.organizer.read_from_filepath()
        self.assertIsNot(0, len(self.organizer.fileData))

    def test_read_input_valid_data(self):
        self.organizer.read_from_filepath()
        self.assertIsNot(0, len(self.organizer.fileData))

    def test_read_input_invalid_data(self):
        self.organizer.acquire_filepath()
        self.organizer.read_from_filepath()
        self.assertIsNot(0, len(self.organizer.fileData))

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")