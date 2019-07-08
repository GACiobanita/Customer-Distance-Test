import os
import json


class FileReader(object):

    def __init__(self):
        self.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.CUSTOMER_FILE = self.ROOT_DIR + '\\' + "customers.txt"
        self.input_file_path = self.CUSTOMER_FILE
        self.data = []

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
                    self.data.append(json.loads(line))
                except ValueError:
                    print("Encountered error for line: " + line)
                    continue
