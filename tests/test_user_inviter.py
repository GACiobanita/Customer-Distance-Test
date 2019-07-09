import unittest
from implementation.user_inviter import UserInviter
from timeit import default_timer as timer

class TestUserInviter(unittest.TestCase):

    def setUp(self):
        self.file_reader = UserInviter()

    def test_paths(self):
        self.file_reader.acquire_filepath()
        message = self.file_reader.CUSTOMER_FILE + " " + self.file_reader.input_file_path
        self.assertNotEqual("None", self.file_reader.input_file_path, message)

    def test_read_input(self):
        self.file_reader.read_from_filepath()
        self.assertIsNot(0, len(self.file_reader.fileData))

    def test_read_input_valid_path(self):
        self.file_reader.acquire_filepath()
        self.file_reader.read_from_filepath()
        self.assertIsNot(0, len(self.file_reader.fileData))

    def test_read_input_invalid_path(self):
        self.file_reader.acquire_filepath()
        self.file_reader.read_from_filepath()
        self.assertIsNot(0, len(self.file_reader.fileData))

    def test_read_input_invalid_data(self):
        self.file_reader.acquire_filepath()
        self.file_reader.read_from_filepath()
        self.assertIsNot(0, len(self.file_reader.fileData))

    def test_create_customer_data(self):
        self.file_reader.acquire_filepath()
        self.file_reader.read_from_filepath()
        self.file_reader.create_customer_data()
        self.assertIsNot(0, len(self.file_reader.customerData))
        for data in self.file_reader.customerData:
            print(data)

    def test_display_customer_data(self):
        self.file_reader.acquire_filepath()
        self.file_reader.read_from_filepath()
        self.file_reader.create_customer_data()
        self.file_reader.display_customer_data()
        self.assertIsNot(0, len(self.file_reader.customerData))

    def test_user_inviter_merge_sort(self):
        self.file_reader.acquire_filepath()
        start = timer()
        self.file_reader.read_from_filepath()
        self.file_reader.create_customer_data()
        self.file_reader.display_customer_data()
        end = timer()
        print("Time: " + str(end-start))


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
