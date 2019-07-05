import os
import json

class FileReader(object):
    
    def __init__(self):
        self.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.CUSTOMER_FILE = self.ROOT_DIR+'\\'+"customers.txt"
        self.input_filePath = self.CUSTOMER_FILE
        self.data = []

    def acquire_filepath(self):
        inputPath=input("Enter the path leading towards the desired file: ")
        if os.path.exists(inputPath) is True:
            self.input_filePath=inputPath
        else:
            print("File path is incorrect, default file will be used instead.")

    def read_from_filepath(self):
        with open(self.input_filePath) as jsonFile:
            for line in jsonFile:
                try:
                    self.data.append(json.loads(line))
                except ValueError as e:
                    print("Encountered error for line: "+line)
                    continue
    