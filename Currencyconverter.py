import requests

usd_amount = int(input("Value : "))
url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()

exchange_rate = data["rates"]["INR"]
inr_amount = usd_amount * exchange_rate

print(f"Given USD is equivalent to {inr_amount} INR")