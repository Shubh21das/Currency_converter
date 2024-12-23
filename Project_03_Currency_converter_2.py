# currency converter using API
# using requests module 

import requests

def currency_converter(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    
    if to_currency in data['rates']:
        rate = data['rates'][to_currency]
        converted_amount = amount * rate
        return converted_amount
    else:
        return f"Conversion rate for {to_currency} not available."

amount = float(input("Enter amount: "))
from_currency = input("From currency (e.g., USD): ").upper()
to_currency = input("To currency (e.g., INR): ").upper()

converted = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} = {converted} {to_currency}")
