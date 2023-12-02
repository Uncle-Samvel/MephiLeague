import json

class Unzipping():
    @staticmethod
    def unzipp_the_tournaments():
        with open('../archive/data/1.json', 'r') as file:
            data = json.load(file)

            return data