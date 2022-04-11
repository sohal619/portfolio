import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

account_sid = "ENTER KEY"
auth_token = 'ENTER KEY'

url = "https://www.amazon.in/Airdopes-441-Technology-Immersive-Resistance/dp/B08T5J6YTQ/ref=sr_1_22?crid" \
      "=1WVYGZ4Y57C15&pd_rd_r=594ca229-e062-4c09-a2e6-1fdc0285dfd3&pd_rd_w=EtDJi&pd_rd_wg=rHgXE&pf_rd_p=f690369a-7bb4" \
      "-48bb-9349-f68a447ef06d&pf_rd_r=R2TGYA0Y6JC6GV2FN9SH&qid=1646421707&smid=A14CZOWI0VEHLG&sprefix=%2Celectronics" \
      "%2C519&sr=8-22&th=1 "

headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

response = requests.get(url=url, headers=headers)

content = response.text

soup = BeautifulSoup(content, "html.parser")
product_title = (soup.select_one("#productTitle")).getText()
price_tag = soup.select_one(".a-offscreen")
price = float(((price_tag.getText()).replace("₹", "")).replace(",", ""))

if price <= 2500.00:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"PRICE ALERT⚠\n{product_title}\nPrice:₹{price}\nVisit:{url}",
        from_="+18065414549",
        to="+918824541747"
    )
    print(message.status)
