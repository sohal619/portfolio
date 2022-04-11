from twilio.rest import Client


class NotificationManager:
    def __init__(self):
        self.account_sid = "ENTRE KEY"
        self.auth_token = "ENTER KEY"

    def messenger(self, price, air_from, city, air_to, date_from, date_to):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=f"Low price alert! Only £{price} to fly from London-{air_from} to {city}-{air_to}, from {date_from} to"
                 f"{date_to}.",
            from_="+18065414549",
            to="+918824541747"
        )
        print(message.status)
