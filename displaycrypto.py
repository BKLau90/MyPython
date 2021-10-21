#description: This program gets the price of crytocurrency in real time

#import libraris 
from re import X
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from requests.models import ContentDecodingError
from rich.console import Console
from rich.table import Column, Table
import json
##############################################################################

#Connection to Coinmarketcap API
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
headers = {
   'Accepts': 'application/json',
   'X-CMC_PRO_API_KEY': '7ec7fdc9-c101-42d2-8011-d91d632549d4',
  }
session = Session()
session.headers.update(headers)

response = session.get(url)
data = json.loads(response.text)

console = Console()

for coin in data['data']:
  symbol = (coin['symbol'])
  rank = (coin['cmc_rank'])
  price =(coin['quote']['USD']['price'])

table = Table (title="My CryptoCurrency Portfolio")
table.add_column("Name", justify="right", style="cyan", no_wrap=True)
table.add_column("Rank", justify="right", style="cyan", no_wrap=True)
table.add_column("Current Price:", justify="right", style="cyan", no_wrap=True)
table.add_row(str(symbol),str(rank),(str(price)))
console.print(table)




