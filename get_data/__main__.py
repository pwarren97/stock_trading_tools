import argparse
import conf
from datetime import datetime, timedelta

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
if args.date[0]:
    start_date = datetime(int(args.date[0][:4]), int(args.date[0][4:6]), int(args.date[0][6:]))

    if len(args.date) == 2:
        end_date = datetime(int(args.date[1][:4]), int(args.date[1][4:6]), int(args.date[1][6:]))
    elif len(args.date) == 1:
        # makes end_date one day ahead of start_date
        end_date = start_date + timedelta(days=1)

# Handle all the options
if args.symbols and (args.date or args.stock): # Stock data and symbols can't be pulled at the same time
    print("You cannot pull stock data and symbols at the same time. Use -h or --help to see the options.")
elif args.symbols: # handle downloading symbols
    symbols = source.get_symbols()
    dbms.save_symbols(symbols)
elif args.stock == None or args.date == None: # handle not having date and stock options together
    print("The stock (-s|--stock) and date (-d|--date) options are required. Use -h or --help to see the options.")
else:
    # Get the historical stock data from the internet
    if start_date < end_date:
        stock_df = source.get_stock_data(args.stock, start_date, end_date, close_only=args.close_only)
        print("Data saved to the database looks as follows:")
        print(stock_df)
        dbms.save_stock_data(stock_df)
    else:
        print("There isn't a date, stock, or the dates aren't in order.")
