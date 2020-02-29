import argparse
import stt_global_items.conf as conf
from datetime import datetime, timedelta
import helpers

if conf.DB == "mongodb":
    from stt_global_items.dbms.mongodb import Mongo as dbms
elif conf.DB == "sql":
    from stt_global_items.dbms.sql import SQL as dbms

# Parse the command line input
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--stock", nargs="+", type=str, help="")
parser.add_argument("-d", "--date", nargs="+", type=str, help="")
parser.add_argument("-i", "--indicators", nargs="+", type=str, help="")
parser.add_argument("--all", help="", action="store_true")
args = parser.parse_args()

if args.indicators:
    if args.date:
        start_date, end_date = helpers.parse_start_and_end_dates(args.date)

    if args.all:
        indicators = helpers.all_indicators
    else:
        indicators = args.indicators

    df = dbms.get_stock_data(args.stock, start_date, end_date)


    if end_date == None:
        indicator_df = helpers.calc_indicators(indicators, start_date)
    elif start_date < end_date:
        indicator_df = helpers.calc_indicators(indicators, start_date, end_date)
    else:
        print("Something went wrong.")
