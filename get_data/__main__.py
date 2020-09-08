import argparse
import stt_global_items.conf as conf
from stt_global_items import global_helpers
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
symbols_option = "--symbols"
close_only_option = "--close_only"

# Parse the command line input
parser = argparse.ArgumentParser()
parser.add_argument(global_helpers.stock_option1, global_helpers.stock_option2, nargs='+', type=str, help=global_helpers.stock_param_help_msg)
parser.add_argument(global_helpers.date_option1, global_helpers.date_option2, nargs='+', type=str, help=global_helpers.date_param_help_msg)
parser.add_argument(symbols_option, help="download symbols if they are not in the database", action="store_true")
parser.add_argument(close_only_option, help="only get close prices", action="store_true")
args = parser.parse_args()

# helpers.validate_input(args)

if args.date:
    start_date, end_date = global_helpers.parse_start_and_end_dates(args.date)

msg_part1 = "If you are aiming to pull stock data, you need to include"


# Handle all the options

# Handle downloading symbols
if args.symbols and not (args.stock or args.date):
    symbols = source.get_symbols()
    dbms.save_symbols(symbols)
# Get the historical stock data from the internet
elif args.stock and args.date and not args.symbols:
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
# Handle errors
else:
    if args.symbols and (args.stock or args.date): # Stock data and symbols can't be pulled at the same time
        print("You cannot pull stock data and symbols at the same time. " + global_helpers.help_msg)
    elif not args.date and not args.stock:
        print(msg_part1 + " the stock (" + global_helpers.stock_option1 + "|" + global_helpers.stock_option2 + ") and date (" + global_helpers.date_option1 + "|" + global_helpers.date_option2 + ") optional parameters. " + global_helpers.help_msg)
    elif args.date and not args.stock:
        print(msg_part1 + " the stock (" + global_helpers.stock_option1 + "|" + global_helpers.stock_option2 + ") optional parameter. " + global_helpers.help_msg)
    elif not args.date and args.stock:
        print(msg_part1 + " the date (" + global_helpers.date_option1 + "|" + global_helpers.date_option2 + ") optional parameter. " + global_helpers.help_msg)
    elif start_data >= end_date:
        print("The start date must come before the end date.")
