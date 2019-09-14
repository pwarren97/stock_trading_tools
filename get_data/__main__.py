import argparse
import conf

# import the appropriate class as source for the source indicated in the conf.py file
if conf.data_source == "iex":
    from sources.iex import IEXCloud as source
# elif conf.data_source == "someotherone":
#     from sources.iex import ThatObject as source

if conf.db == "mongodb":
    from dbms.mongodb import Mongo as dbms
elif conf.db == "sql":
    from dbms.sql import SQL as dbms
    
# Parse the command line input
parser = argparse.ArgumentParser("get_data.sh")
parser.add_argument("-s", "--stock", nargs='+', type=str, help="what stock(s) to download. input should be ticker symbols")
parser.add_argument("-d", "--date", nargs='+', type=str, help="takes start date or start and end dates for stock data in format yyyymmdd")
args = parser.parse_args()

# If the options weren't entered right
if args.stock == None or args.date == None:
    print("The stock (-s|--stock) and date (-d|--date) options are required. Use -h or --help to see the options.")
else:
    # Get the historical stock data from the internet
    stock_data = None

    if len(args.date) == 1:
        stock_data = source.get_stock_data(args.stock, args.date[0])
    elif len(args.date) == 2 and int(args.date[0]) < int(args.date[1]):
        stock_data = source.get_stock_data(args.stock, args.date[0], args.date[1])
    else:
        print("There either isn't a date or a stock.")

    print(stock_data)


# Pass the data off to the database
