#description: This program gets the price of crytocurrency in real time

#import libraris 
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
#this line calls the coinmarketcap API to grab the current price of the BTC

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '7ec7fdc9-c101-42d2-8011-d91d632549d4',
}

#assign the results to variable data
data = response.json()

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

