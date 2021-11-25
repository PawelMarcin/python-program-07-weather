
import json


class FileHandling:
    def __init__(self, file):
        self.file = file
        self.object = {}

    def open_json(self):
        with open(self.file, 'r') as file:
            self.object = json.load(file)

    def save_json(self):
        with open(self.file, 'w') as file:
            json.dump(self.object, file, ensure_ascii=False, sort_keys=self.object.keys())
