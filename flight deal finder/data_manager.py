import requests


class DataManager:
    def __init__(self):
        self.posting_data = {}
        self.url = "https://api.sheety.co/99e2ea277f94e9b39b8a6255ed623cb4/flightDeals/sheet1/"

    def code_updater(self, row: str, code: str):
        self.posting_data = {
            "sheet1": {
                "iataCode": code
            }
        }
        requests.put(url=self.url + row, json=self.posting_data)
