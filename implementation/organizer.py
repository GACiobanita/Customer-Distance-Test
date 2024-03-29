import json
import os

#The Organizer class will take the JSON file and verify if it is valid
#It will either use a file passed by the user or the default one, as part
#of the project

class Organizer(object):

    def __init__(self):
        self.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.CUSTOMER_FILE = self.ROOT_DIR + '\\' + "customers.txt"
        self.input_file_path = self.CUSTOMER_FILE
        self.fileData = []

    def acquire_filepath(self):
        input_path = input("Enter the path leading towards the desired file: ")
        if os.path.exists(input_path) is True:
            self.input_file_path = input_path
        else:
            print("Passed file path is incorrect, default file will be used instead.")

    def read_from_filepath(self):
        with open(self.input_file_path) as jsonFile:
            for line in jsonFile:
                try:
                    self.fileData.append(json.loads(line))
                except ValueError:
                    print("Data is not valid JSON: " + line)
                    continue
