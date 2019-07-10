import unittest
from implementation.user_inviter import UserInviter
from timeit import default_timer as timer

class TestUserInviter(unittest.TestCase):

    def setUp(self):
        self.file_reader = UserInviter()

    def test_create_customer_data_valid(self):
        data = []
        data.append({"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"})
        self.file_reader.create_customer_data(data)
        self.assertIsNot(0, self.file_reader.bst.nodeCount)

    def test_create_customer_data_invalid(self):
        data = []
        data.append({"laitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"})
        data.append({"latitude": "52.986375", "user_id": 12, "ame": "Christina McArdle", "longitude": "-6.043701"})
        data.append({"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"})
        self.file_reader.create_customer_data(data)
        self.assertIsNot(0, self.file_reader.bst.nodeCount)

    def test_user_inviter_bst(self):
        data = []
        data.append({"latitude": "52.986375", "user_id": 12, "name": "Christina MArdle", "longitude": "-6.043701"})
        data.append({"latitude": "52.989375", "user_id": 14, "name": "Christina McArle", "longitude": "-6.043701"})
        data.append({"latitude": "52.986315", "user_id": 15, "name": "Christina McArde", "longitude": "-6.043701"})
        start = timer()
        self.file_reader.create_customer_data()
        self.file_reader.display_customer_data()
        end = timer()
        print("Time: " + str(end - start))

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")