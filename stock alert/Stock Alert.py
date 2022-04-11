import requests
from twilio.rest import Client


def send_sms(s):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"TSLA: {s}{abs(percent)}%\nHeadline: {heading}\nBrief: {brief}",
        from_="+18065414549",
        to="+918824541747")
    print(message.status)


account_sid = "ENTER KEY"
auth_token = "ENTER KEY"
c = []
STOCK_up = "🔺"
STOCK_down = "🔻"

COMPANY_NAME = "Tesla Inc"


response = requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY"
                            "&symbol=TSLA&"
                            "apikey=EKT9QP2J1PF42QW2")
data = response.json()
di = data["Time Series (Daily)"]
for a in di:
    b = di[a]["4. close"]
    c.append(b)

price1 = float(c[0])
price2 = float(c[1])
difference = price1 - price2
percent = round((difference/price2)*100)

up = price2+((price2*5)/100)
down = price2-((price2*5)/100)

response2 = requests.get(url="https://newsapi.org/v2/everything?qInTitle=Tesla Inc&"
                             "apiKey=39d1eed22ecb43ba804e8522dfa973d6")
data2 = response2.json()
heading = data2["articles"][0]["title"]
brief = data2["articles"][0]["description"]
if percent < 0:
    send_sms(STOCK_up)
elif percent > 0:
    send_sms(STOCK_down)
