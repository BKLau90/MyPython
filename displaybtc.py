#description: This program gets the price of crytocurrency in real time

#import library to allow sent HTTP requests using Python
import requests

#this line calls the coindesk API to grab the current price of the cryto coin
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

#assign the results to variable data
data = response.json()

#display the data 
print ("BTC Current Price is ")
print(data["bpi"]["USD"]["rate"] )

