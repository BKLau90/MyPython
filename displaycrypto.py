# description: This program gets the price of crytocurrency in real time

# import libraries
import configparser
from os import PRIO_PROCESS
import requests
from rich.console import Console
from rich.table import Column, Table
from rich.live import Live
from configparser import ConfigParser
import argparse
import json
##############################################################################

api_request = requests.get(
    "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd")
api_response = json.loads(api_request.content)

my_portfolio = [
    {
        "sym": "btc"
    },
    {
        "sym": "eth"
    },
    {
        "sym": "xrp"
    }


]
console = Console()
table = Table(title="My CryptoCurrency Portfolio")
table.add_column("Name", justify="center", style="cyan", no_wrap=True)
table.add_column("Rank", justify="center", style="cyan", no_wrap=True)
table.add_column("Price", justify="center", style="cyan", no_wrap=True)
for coin in api_response:
    for mycoin in my_portfolio:
        if mycoin["sym"] == coin["symbol"]:
            name = coin["name"]
            rank = coin["market_cap_rank"]
            price = "${:,.2f}".format(coin["current_price"])
            table.add_row(str(name), str(rank), str(price))
console.print(table)
