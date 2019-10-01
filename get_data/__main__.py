import argparse
import conf

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
args = parser.parse_args()

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
        stock_data = source.get_stock_data(args.stock, args.date[0])
        dbms.save_stock_data([stock_data])
    elif len(args.date) == 2 and int(args.date[0]) < int(args.date[1]):
        stock_data = source.get_stock_data(args.stock, args.date[0], args.date[1])
        dbms.save_stock_data([stock_data])
    else:
        print("There either isn't a date or a stock.")


# Pass the data off to the database
