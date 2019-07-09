import unittest
from implementation.user_inviter import UserInviter


class TestUserInviter(unittest.TestCase):

    def setUp(self):
        self.file_reader = UserInviter()

    def test_paths(self):
        self.file_reader.acquire_filepath()
        message = self.file_reader.CUSTOMER_FILE + " " + self.file_reader.input_file_path
        self.assertNotEqual("None", self.file_reader.input_file_path, message)
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
        print("test_read_input_valid_path: " + self.file_reader.input_file_path)

    def test_read_input_invalid_path(self):
        self.file_reader.acquire_filepath()
        self.file_reader.read_from_filepath()
        self.assertIsNot(0, len(self.file_reader.data))
        print("test_read_input_invalid_path: " + self.file_reader.input_file_path)

    def test_read_input_invalid_data(self):
        self.file_reader.acquire_filepath()
        self.file_reader.read_from_filepath()
        self.assertIsNot(0, len(self.file_reader.data))
        print("test_read_input_invalid_path: " + self.file_reader.input_file_path)

    def test_create_customer_data(self):
        self.file_reader.acquire_filepath()
        self.file_reader.read_from_filepath()
        self.file_reader.create_customer_data()
        for data in self.file_reader.customerData:
            print(data)

    def test_display_customer_data(self):
        self.file_reader.acquire_filepath()
        self.file_reader.read_from_filepath()
        self.file_reader.create_customer_data()
        self.file_reader.display_customer_data()
        for data in self.file_reader.customerData:
            print(data)


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
