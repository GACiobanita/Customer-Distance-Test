import os
import json
from .customer import Customer
from .coordinate import Coordinate
from . import distance_calc
from .algorithms import BST

class UserInviter(object):

    def __init__(self):
        self.customerData = []
        self.bst = BST()

    def create_customer_data(self, fileData):
        for data in fileData:
            if UserInviter.check_json_data(data) is True:
                customer_location = Coordinate(float(data.get("latitude")), float(data.get("longitude")))
                if distance_calc.distance(customer_location) <= 100:
                    self.bst.insert(
                        Customer(
                            data.get("user_id"), data.get("name"), customer_location
                        )
                    )
            else:
                print("Found invalid json key for latitude/longitude, will skip the following line:" + str(data))

    def display_customer_data(self):
        self.customerData = self.bst.inorder_traversal(self.bst.root)
        for customer in self.customerData:
            print(customer)

    def check_json_data(data):
        if data.get("latitude") is None:
            return False
        if data.get("longitude") is None:
            return False
        if data.get("user_id") is None:
            return False
        if data.get("name") is None:
            return False
        return True
