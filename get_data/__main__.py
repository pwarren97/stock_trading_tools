import argparse
import conf
from datetime import datetime

# import the appropriate source and dbms as indicated in the conf.py file
if conf.DATA_SOURCE == "iex":
    from sources.iex import IEXCloud as source
# elif conf.DATA_SOURCE == "someotherone":
#     from sources.iex import ThatObject as source

if conf.DB == "mongodb":
    from dbms.mongodb import Mongo as dbms
elif conf.DB == "sql":
    from dbms.sql import SQL as dbms

# Parse the command line input
parser = argparse.ArgumentParser("get_data.sh")
parser.add_argument("-s", "--stock", nargs='+', type=str, help="what stock(s) to download. input should be ticker symbols")
parser.add_argument("-d", "--date", nargs='+', type=str, help="takes start date or start and end dates for stock data in format yyyymmdd")
parser.add_argument("--symbols", help="download symbols if they are not in the database", action="store_true")
parser.add_argument("--close_only", help="only get close prices", action="store_true")
args = parser.parse_args()


# create start and end date datetime.date objects
start_date = datetime(int(args.date[0][:4]), int(args.date[0][4:6]), int(args.date[0][6:]))
if len(args.date) == 2:
    end_date = datetime(int(args.date[1][:4]), int(args.date[1][4:6]), int(args.date[1][6:]))

# If the options weren't entered right
if args.symbols:
    symbols = source.get_symbols()
    dbms.save_symbols(symbols)
elif args.stock == None or args.date == None:
    print("The stock (-s|--stock) and date (-d|--date) options are required. Use -h or --help to see the options.")
else:
    # Get the historical stock data from the internet
    stock_data = None

    # Single date passed through -d | --date optional argument
    if len(args.date) == 1:
        stock_data = source.get_stock_data(args.stock, start_date, close_only=args.close_only)
        dbms.save_stock_data(stock_data)
    elif len(args.date) == 2 and int(args.date[0]) < int(args.date[1]):
        stock_data = source.get_stock_data(args.stock, start_date, end_date, close_only=args.close_only)
        dbms.save_stock_data(stock_data)
    else:
        print("There isn't a date, stock, or the dates aren't in order.")


# Pass the data off to the database
