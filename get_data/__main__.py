from os import sys
import argparse
import conf
from sources import iex

# parse the command line input
parser = argparse.ArgumentParser("get_data.sh")
parser.add_argument("-s", "--stock", nargs='+', type=str, help="what stock(s) to download. input should be ticker symbols")
parser.add_argument("-d", "--date", nargs='+', type=str, help="takes start date or start and end dates for stock data in format yyyymmdd")
args = parser.parse_args()
print(args.stock)
print(args.date)


# Get the historical stock data from the internet
stock_data = None

if len(args.date) == 1:
    stock_data = iex.get_stock_data(args.stock, args.date[0])
elif len(args.date) == 2:
    stock_data = iex.get_stock_data(args.stock, args.date[0], args.date[1])
else:
    print("There either isn't a date or a stock.")

# if stock_data.any():
print(stock_data)
