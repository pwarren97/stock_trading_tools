import argparse
import stt_global_items.conf as conf
from datetime import datetime, timedelta
import helpers
from stt_global_items import global_helpers

if conf.DB == "mongodb":
    from stt_global_items.dbms.mongodb import Mongo as dbms
elif conf.DB == "sql":
    from stt_global_items.dbms.sql import SQL as dbms

# set up string variables to represent the optional parameters' names
indicators_option1, indicators_option2 = "-i", "--indicators"
all_indicators_option = "--all_indicators"

# Parse the command line input
parser = argparse.ArgumentParser()
parser.add_argument(global_helpers.stock_option1, global_helpers.stock_option2, nargs="+", type=str, help="")
parser.add_argument(global_helpers.date_option1, global_helpers.date_option2, nargs="+", type=str, help="")
parser.add_argument(indicators_option1, indicators_option2, nargs="+", type=str, help="")
parser.add_argument(all_indicators_option, help="", action="store_true")
args = parser.parse_args()



indicators_msg = "The indicators available for use is as follows:";
def print_available_indicators():
    for item in helpers.all_indicators:
        print("\t" + item)

if (args.indicators or args.all_indicators) and args.date and args.stock:
    start_date, end_date = global_helpers.parse_start_and_end_dates(args.date)

    if args.all_indicators:
        indicators = helpers.all_indicators
    else:
        for item in args.indicators:
            if item not in helpers.all_indicators:
                print("You have listed an indicator that is not implemented. " + indicators_msg)
                print_available_indicators()
        indicators = args.indicators

    df = dbms.get_stock_data(args.stock, start_date, end_date)

    ind_gen = helpers.IndicatorGenerator(indicators)

    if end_date == None:
        indicator_df = ind_gen.calc_indicators(start_date)
    elif start_date < end_date:
        indicator_df = ind_gen.calc_indicators(start_date, end_date)
    elif start_date > end_date:
        print("The start date should come before the end date.")

    if indicator_df:
        dbms.save_indicators(indicator_df)
    else:
        print("Something went wrong. #2")
else:
    msg_part1 = "You need to specify "
    date_msg = "the date with " + global_helpers.date_option1 + " or " + global_helpers.date_option2
    stock_msg = "the stock with " + global_helpers.stock_option1 + " or " + global_helpers.stock_option2

    if args.date and args.stock:
        print(msg_part1 + "what indicators you want to use with " + indicators_option1 + ", " + indicators_option2 + ", or --all_indicators. " + global_helpers.help_msg)
        print("")
        print(indicators_msg)
        print_available_indicators()
    elif (args.indicators or args.all_indicators) and args.date:
        print(msg_part1 + date_msg + ". "+ global_helpers.help_msg)
    elif (args.indicators or args.all_indicators) and args.stock:
        print(msg_part1 + stock_msg + ". " + global_helpers.help_msg)
    elif (args.indicators or args.all_indicators):
        print(msg_part1 + date_msg + "or " + stock_msg + ". " + global_helpers.help_msg)
