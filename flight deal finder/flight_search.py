import requests


class FlightSearch:
    def __init__(self):
        self.header = {
            "apikey": "ZhX4-3iSUPqXF9PIjA8hFkNb4KjJJWII",
        }

    def code_finder(self, city: str):
        end_point = f"https://tequila-api.kiwi.com/locations/query?term={city}"
        response = requests.get(url=end_point, headers=self.header)
        data = response.json()
        code = data["locations"][0]["code"]
        return code
