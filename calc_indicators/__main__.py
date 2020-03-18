import argparse
import stt_global_items.conf as conf
from datetime import datetime, timedelta
import helpers

if conf.DB == "mongodb":
    from stt_global_items.dbms.mongodb import Mongo as dbms
elif conf.DB == "sql":
    from stt_global_items.dbms.sql import SQL as dbms

# set up string variables to represent the optional parameters' names
stock_option1, stock_option2 = "-s", "--stock"
date_option1, date_option2 = "-d", "--date"
indicators_option1, indicators_option2 = "-i", "--indicators"
all_indicators_option = "--all_indicators"

# Parse the command line input
parser = argparse.ArgumentParser()
parser.add_argument(stock_option1, stock_option2, nargs="+", type=str, help="")
parser.add_argument(date_option1, date_option2, nargs="+", type=str, help="")
parser.add_argument(indicators_option1, indicators_option2, nargs="+", type=str, help="")
parser.add_argument(all_indicators_option, help="", action="store_true")
args = parser.parse_args()



indicators_msg = "The indicators available for use is as follows:";
def print_available_indicators():
    for item in helpers.all_indicators:
        print("\t" + item)

if (args.indicators or args.all_indicators) and args.date and args.stock:
    start_date, end_date = helpers.parse_start_and_end_dates(args.date)

    if args.all_indicators:
        indicators = helpers.all_indicators
    else:
        for item in args.indicators:
            if item not in helpers.all_indicators:
                print("You have listed an indicator that is not implemented. " + indicators_msg)
                print_available_indicators()
        indicators = args.indicators

    df = dbms.get_stock_data(args.stock, start_date, end_date)


    if end_date == None:
        indicator_df = helpers.calc_indicators(indicators, start_date)
    elif start_date < end_date:
        indicator_df = helpers.calc_indicators(indicators, start_date, end_date)
    elif start_date > end_date:
        print("The start date should come before the end date.")

    if indicator_df:
        dbms.save_indicators(indicator_df)
    else:
        print("Something went wrong. #2")
else:
    msg_part1 = "You need to specify "
    date_msg = "the date with " + date_option1 + " or " + date_option2
    stock_msg = "the stock with " + stock_option1 + " or " + stock_option2
    help_msg = "Use calc-indicators -h for help."
    if args.date and args.stock:
        print(msg_part1 + "what indicators you want to use with " + indicators_option1 + ", " + indicators_option2 + ", or --all_indicators. " + help_msg)
        print("")
        print(indicators_msg)
        print_available_indicators()
    elif (args.indicators or args.all_indicators) and args.date:
        print(msg_part1 + date_msg + ". "+ help_msg)
    elif (args.indicators or args.all_indicators) and args.stock:
        print(msg_part1 + stock_msg + ". " + help_msg)
    elif (args.indicators or args.all_indicators):
        print(msg_part1 + date_msg + "or " + stock_msg + ". " + help_msg)
