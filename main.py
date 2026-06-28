import requests
import json
import pyttsx3
import time

URL = "https://api.api-ninjas.com/v1/bitcoin"
PARAMS ={
   "X-Api-Key" : "6v1Q63g8dVSFO7bR3E3iYHvgGO8e2B8WF16BssHT" # Log in to https://api-ninjas.com/api/bitcoin#bitcoin-endpoint
} 

engine = pyttsx3.init()

r = requests.get(url=URL, params=PARAMS)

data = json.loads(r.text)
btc_price = int(float(data["price"]))

engine.say("BTC price is {}".format(btc_price))
print("BTC price is {}".format(btc_price))
engine.runAndWait()
