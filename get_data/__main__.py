import argparse
import stt_global_items.conf as conf
from datetime import datetime, timedelta
import helpers

# import the appropriate source and dbms as indicated in the conf.py file
if conf.DATA_SOURCE == "iex":
    from sources.iex import IEXCloud as source
# elif conf.DATA_SOURCE == "someotherone":
#     from sources.iex import ThatObject as source

if conf.DB == "mongodb":
    from stt_global_items.dbms.mongodb import Mongo as dbms
elif conf.DB == "sql":
    from stt_global_items.dbms.sql import SQL as dbms


# Specify the name of the options
stock_option1, stock_option2 = "-s", "--stock"
date_option1, date_option2 = "-d", "--date"

# Parse the command line input
parser = argparse.ArgumentParser()
parser.add_argument(stock_option1, stock_option2, nargs='+', type=str, help="what stock(s) to download. input should be ticker symbols")
parser.add_argument(date_option1, date_option2, nargs='+', type=str, help="takes start date or start and end dates for stock data in format yyyymmdd")
parser.add_argument("--symbols", help="download symbols if they are not in the database", action="store_true")
parser.add_argument("--close_only", help="only get close prices", action="store_true")
args = parser.parse_args()

# helpers.validate_input(args)

if args.date:
    start_date, end_date = helpers.parse_start_and_end_dates(args.date)

msg_part1 = "If you are aiming to pull stock data, you need to include"
help_msg = "Use -h or --help to see the options."

# Handle all the options

if args.symbols and not (args.stock or args.date): # handle downloading symbols
    symbols = source.get_symbols()
    dbms.save_symbols(symbols)
elif args.stock and args.date and not args.symbols:
    # Get the historical stock data from the internet
    if end_date == None:
        stock_df = source.get_stock_data(args.stock, start_date, close_only=args.close_only)
    elif start_date < end_date:
        stock_df = source.get_stock_data(args.stock, start_date, end_date, close_only=args.close_only)

    # Save data pulled from the database
    if "stock_df" in locals():
        if not stock_df.empty:
            print("New data saved to the database looks as follows:")
            print(stock_df)
        else:
            print("No new data to add to the database.")
        dbms.save_stock_data(stock_df)
else:
    if args.symbols and (args.stock or args.date): # Stock data and symbols can't be pulled at the same time
        print("You cannot pull stock data and symbols at the same time. " + help_msg)
    elif not args.date and not args.stock:
        print(msg_part1 + " the stock (" + stock_option1 + "|" + stock_option2 + ") and date (" + date_option1 + "|" + date_option2 + ") optional parameters. " + help_msg)
    elif args.date and not args.stock:
        print(msg_part1 + " the stock (" + stock_option1 + "|" + stock_option2 + ") optional parameter. " + help_msg)
    elif not args.date and args.stock:
        print(msg_part1 + " the date (" + date_option1 + "|" + date_option2 + ") optional parameter. " + help_msg)
    elif start_data >= end_date:
        print("The start date must come before the end date.")
