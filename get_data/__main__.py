from os import sys
import argparse
import conf
from sources import iex

# parse the command line input
parser = argparse.ArgumentParser("get_data.sh")
parser.add_argument("-s", "--stock", nargs='+', type=str, help="what stock(s) to download. input should be ticker symbols")
parser.add_argument("-d", "--date", nargs='+', type=str, help="takes start date or start and end dates for stock data in format yyyymmdd")
args = parser.parse_args()
# print(args.stock)
# print(args.date)

if args.stock == None or args.date == None:
    print("The stock (-s|--stock) and date (-d|--date) options are required. Use -h or --help to see the options.")
else:
    # Get the historical stock data from the internet
    stock_data = None

    if len(args.date) == 1:
        stock_data = iex.IEXCloud.get_stock_data(args.stock, args.date[0])
    elif len(args.date) == 2 and int(args.date[0]) < int(args.date[1]):
        stock_data = iex.IEXCloud.get_stock_data(args.stock, args.date[0], args.date[1])
    else:
        print("There either isn't a date or a stock.")

    print(stock_data)
