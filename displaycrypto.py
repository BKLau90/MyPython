# description: This program gets the price of crytocurrency in real time

# import libraries
import configparser
from os import PRIO_PROCESS
import requests
from rich.console import Console
from rich.table import Column, Table
from configparser import ConfigParser
import argparse
import json
##############################################################################

api_request = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd")
api_response = json.loads(api_request.content)
my_portfolio = [
    {
        "sym": "btc"
    }
]
for coin in api_response:
    for mycoin in my_portfolio:
        if mycoin["sym"] == coin["symbol"]:
            crypt_coin = coin["name"]
            rank = coin["market_cap_rank"]
            price = coin["current_price"]

console = Console()           
table = Table(title="My CryptoCurrency Portfolio")
table.add_column("Name", justify="right", style="cyan", no_wrap=True)
table.add_column("Rank", justify="right", style="cyan", no_wrap=True)
table.add_column("Price", justify="right", style="cyan", no_wrap=True)
table.add_row(str(crypt_coin), str(rank), (str(price)))
console.print(table)
