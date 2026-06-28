import requests
import json
import pyttsx3
import time

URL = "https://api.api-ninjas.com/v1/bitcoin"
PARAMS ={
   "X-Api-Key" : "ENTER YOUR OWN API KEY HERE." # Log in to https://api-ninjas.com/api/bitcoin#bitcoin-endpoint
} 

class BTC:
    def __init__(self):
        self.engine = pyttsx3.init()

    def get_btc_price(self):
        r = requests.get(url=URL, params=PARAMS)
        data = json.loads(r.text)
        btc_price = int(float(data["price"]))
        self.engine.say("BTC price is {}".format(btc_price))
        print("BTC price is {}".format(btc_price))
        self.engine.runAndWait()


btc = BTC()

btc.get_btc_price()