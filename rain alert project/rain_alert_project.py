import requests
from twilio.rest import Client

account_sid = "ENTRE KEY"
auth_token = "ENTRE KEY"

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?"
                            "lat=26.9167&lon=75.8167&exclude=current,minutely,daily"
                            "&appid=6cc87e5600f90ee8832f5c9ab682b7ea")

response.raise_for_status()
weather_data = response.json()

weather_con = weather_data["hourly"][:12]

for code in weather_con:
    weather_code = code["weather"][0]["id"]
    if 500 <= weather_code < 600:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="Its going to rain today, bring an umbrella🌧🌧☔",
            from_="+18065414549",
            to="+918824541747"
        )
        print(message.status)
        break
