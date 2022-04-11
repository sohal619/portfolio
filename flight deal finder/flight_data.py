import requests
from datetime import datetime, timedelta


class FlightData:
    def __init__(self):
        self.header = {
            "apikey": "ZhX4-3iSUPqXF9PIjA8hFkNb4KjJJWII"
        }
        now = datetime.now()
        day = now.date().strftime("%d")
        a = int(day) + 1
        self.date_from = now.date().strftime(f"{a}/%m/%Y")
        self.date_to = (now.date() + timedelta(days=180)).strftime("%d/%m/%Y")

    def expanse(self, code: str):
        url = f"https://tequila-api.kiwi.com/v2/search?fly_from=LON&fly_to={code}&date_from={self.date_from}&" \
              f"date_to={self.date_to}&curr=GBP"
        response = requests.get(url=url, headers=self.header)
        data = response.json()
        try:
            price = data["data"][0]["price"]
            fly_from = data["data"][0]["flyFrom"]
            fly_to = data["data"][0]["flyTo"]
        except IndexError:
            return ()
        else:
            return price, fly_from, fly_to
