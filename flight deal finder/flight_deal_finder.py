import requests
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager


f_s_data = FlightSearch()
d_data = DataManager()
f_data = FlightData()
n_data = NotificationManager()

response = requests.get(url="https://api.sheety.co/99e2ea277f94e9b39b8a6255ed623cb4/flightDeals/sheet1")
data = response.json()
sheet_data = data["sheet1"]

# to get iata code and update them into the spreadsheet table
# for _ in range(len(sheet_data)):
#     iata_code = f_s_data.code_finder(sheet_data[_]["city"])
#     d_data.code_updater(str(sheet_data[_]["id"]), iata_code)


for _ in sheet_data:
    if f_data.expanse(_['iataCode']) == ():
        continue
    else:
        price = f_data.expanse(_['iataCode'])[0]
        if price <= _["lowestPrice"]:
            n_data.messenger(price=price, air_from=f_data.expanse(_['iataCode'])[1],
                             air_to=f_data.expanse(_['iataCode'])[2], city=_["city"], date_from=f_data.date_from,
                             date_to=f_data.date_to)
