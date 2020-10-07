import argparse
import stt_lib.conf as conf
from datetime import datetime, timedelta
import calc_indicators.helpers as helpers
from stt_lib import global_helpers
from stt_lib.indicators.generator import IndicatorGenerator
from stt_lib.dbms.helpers import import_dbms
import pandas as pd

dbms = import_dbms()


# Parse the command line input
parser = argparse.ArgumentParser()
args = helpers.parse_arguments(parser)


# Input validation
# If there exists an input that is also valid, the variables will be True
valid_date = (args.date is not None) and global_helpers.validate_date_param(args.date)
valid_stock = (args.stock is not None) and global_helpers.validate_stock_param(args.stock)
valid_indicators = (args.indicators is not None) and helpers.validate_ind_param(args.indicators)
valid_sets = (args.set is not None) and helpers.validate_set_param(args.set)


# Handle options
# Handle a valid request to generate indicators
if valid_date and valid_stock and (valid_sets ^ valid_indicators ^ args.all_indicators):
    # Parse the dates and then pull the data from the db
    start_date, end_date = global_helpers.parse_start_and_end_dates(args.date)
    db_data = dbms.get_stock_data(args.stock, start_date, end_date)

    # Set up the indicator generator
    if args.set:
        ind_gen = IndicatorGenerator(db_data, helpers.parse_sets(args.set))
    elif args.indicators:
        ind_gen = IndicatorGenerator(db_data, helpers.parse_indicators(args.indicators))
    else:
        ind_gen = IndicatorGenerator(db_data, helpers.parse_indicators(helpers.all_indicators))

    # Generate indicators
    indicator_df = pd.DataFrame()
    if end_date == None:
        indicator_df = ind_gen.calc_indicators(start_date)
    elif start_date < end_date:
        indicator_df = ind_gen.calc_indicators(start_date, end_date)
    elif start_date >= end_date:
        print("The start date should come before the end date.")

    if not indicator_df.empty:
        dbms.save_indicators(indicator_df)
    else:
        print("No data was saved to the database")
# Handle errors
else:
    msg_part1 = "You need to specify "
    date_msg = "the date with (" + global_helpers.date_option1 + "|" + global_helpers.date_option2 + ")"
    stock_msg = "the stock with (" + global_helpers.stock_option1 + "|" + global_helpers.stock_option2 + ")"

    # missing indicator option
    if args.date and args.stock:
        print(msg_part1 + "what indicators you want to use with (" + helpers.indicators_option1 + "|" + helpers.indicators_option2 + ") or " + helpers.all_indicators_option + ". " + global_helpers.help_msg)
        print("")
        helpers.print_available_indicators()
    # missing stock option
    elif (args.indicators or args.all_indicators) and args.date:
        print(msg_part1 + stock_msg + ". "+ global_helpers.help_msg)
    # missing date parameter
    elif (args.indicators or args.all_indicators) and args.stock:
        print(msg_part1 + date_msg + ". " + global_helpers.help_msg)
    # missing date and stock parameters
    elif (args.indicators or args.all_indicators):
        print(msg_part1 + date_msg + "or " + stock_msg + ". " + global_helpers.help_msg)
