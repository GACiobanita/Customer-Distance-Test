import unittest
from FileReader import FileReader

class TestFileReader(unittest.TestCase):

    def setUp(self):
        self.fileReader=FileReader()
    
    def test_paths(self):
        self.fileReader.acquire_filepath()
        message=self.fileReader.CUSTOMER_FILE+" "+self.fileReader.input_filePath
        self.assertNotEqual("None", self.fileReader.input_filePath, message)
        print("test_paths: " + message)
        
    def test_read_input(self):
       self.fileReader.read_from_filepath()
       self.assertIsNot(0, len(self.fileReader.data))
       print("test_read_input: ")
       print(self.fileReader.data)

    def test_read_input_valid_path(self):
         self.fileReader.acquire_filepath()
         self.fileReader.read_from_filepath()
         self.assertIsNot(0, len(self.fileReader.data))
         print("test_read_input_valid_path: " + self.fileReader.input_filePath)

    def test_read_input_invalid_path(self):
        self.fileReader.acquire_filepath()
        self.fileReader.read_from_filepath()
        self.assertIsNot(0, len(self.fileReader.data))
        print("test_read_input_invalid_path: " + self.fileReader.input_filePath)

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")