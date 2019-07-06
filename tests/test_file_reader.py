import unittest
from implementation.file_reader import FileReader

class TestFileReader(unittest.TestCase):

    def set_up(self):
        self.file_reader=FileReader()
    
    def test_paths(self):
        self.file_reader.acquire_filepath()
        message=self.file_reader.CUSTOMER_FILE+" "+self.file_reader.input_filePath
        self.assertNotEqual("None", self.file_reader.input_filePath, message)
        print("test_paths: " + message)
        
    def test_read_input(self):
       self.file_reader.read_from_filepath()
       self.assertIsNot(0, len(self.file_reader.data))
       print("test_read_input: ")
       print(self.file_reader.data)

    def test_read_input_valid_path(self):
        self.file_reader.acquire_filepath()
        self.file_reader.read_from_filepath()
        self.assertIsNot(0, len(self.file_reader.data))
        print("test_read_input_valid_path: " + self.file_reader.input_filePath)

    def test_read_input_invalid_path(self):
        self.file_reader.acquire_filepath()
        self.file_reader.read_from_filepath()
        self.assertIsNot(0, len(self.file_reader.data))
        #print("test_read_input_invalid_path: " + self.file_reader.input_filePath)

    def test_read_input_invalid_data(self):
        self.file_reader.acquire_filepath()
        self.file_reader.read_from_filepath()
        self.assertIsNot(0, len(self.file_reader.data))
        print("test_read_input_invalid_path: " + self.file_reader.input_filePath)

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")