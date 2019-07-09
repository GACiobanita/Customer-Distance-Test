import os
import json
from .customer import Customer
from .coordinate import Coordinate
from . import distance_calc
from .algorithms import quick_sort

class UserInviter(object):

    def __init__(self):
        self.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.CUSTOMER_FILE = self.ROOT_DIR + '\\' + "customers.txt"
        self.input_file_path = self.CUSTOMER_FILE
        self.fileData = []
        self.customerData = []

    def acquire_filepath(self):
        input_path = input("Enter the path leading towards the desired file: ")
        if os.path.exists(input_path) is True:
            self.input_file_path = input_path
        else:
            print("File path is incorrect, default file will be used instead.")

    def read_from_filepath(self):
        with open(self.input_file_path) as jsonFile:
            for line in jsonFile:
                try:
                    self.fileData.append(json.loads(line))
                except ValueError:
                    print("Encountered error for line: " + line)
                    continue

    def create_customer_data(self):
        for data in self.fileData:
            customer_location = Coordinate(float(data.get("latitude")), float(data.get("longitude")))
            if distance_calc.distance(customer_location) <= 100:
                self.customerData.append(
                    Customer(
                        data.get("user_id"), data.get("name"), customer_location
                    )
                )

    def display_customer_data(self):
        quick_sort(self.customerData, 0, len(self.customerData)-1)
        for customer in self.customerData:
            print(customer)
