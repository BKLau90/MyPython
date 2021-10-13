#description: This program gets the price of crytocurrency in real time

#import libraris 
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

#connect to coinmarketcap API to grab the current price of the BTC
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

#define the API key 
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '7ec7fdc9-c101-42d2-8011-d91d632549d4',
}
#define the parameters/info to be pulled from the API 
parameters = {
  'symbol':'BTC',
  'convert':'USD'
}
#store persistent data for web requests
session = Session()
session.headers.update(headers)

#Define the API response based on the parameters provided and only print the price of the BTC using nested json keys
try:
  response = session.get(url, params=parameters)
  data = response.json()
  print("Latest BTC Price in US Dollar is  ")
  print(data["data"]["BTC"]["quote"]["USD"]["price"])
  
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

