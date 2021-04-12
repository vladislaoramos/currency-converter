import requests
import json


CHECKING_CACHE = "Checking the cache..."
IN_CACHE = "Oh! It is in the cache!"
NOT_IN_CACHE = "Sorry, but it is not in the cache!"


currency_code = input().lower()
url = "http://www.floatrates.com/daily/" \
      + currency_code \
      + ".json"
response = json.loads(requests.get(url).text)
cache = dict()

if currency_code != "eur":
    cache["eur"] = float(response["eur"]["rate"])
if currency_code != "usd":
    cache["usd"] = float(response["usd"]["rate"])

while True:
    received_code = input().lower()
    if not received_code:
        break
    amount = int(input())
    print(CHECKING_CACHE)
    received_rate = float(response[received_code]['rate'])
    if received_code in cache.keys():
        print(IN_CACHE)
    else:
        print(NOT_IN_CACHE)
        cache[received_code] = received_rate
    money = round(amount * received_rate, 2)
    currency = received_code.upper()
    print("You received ", money, " ", currency, ".", sep='')
