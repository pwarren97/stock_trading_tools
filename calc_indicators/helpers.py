# This file has helpers for __main__.py
import pandas as pd
from datetime import datetime
from indicators.model import Indicator
from indicators.ema import EMA
from indicators.macd import MACD
from stt_global_items import global_helpers
import argparse

all_indicators = \
[
"EMA",
"MACD",
"RoC",
"SRoC",
"W%R"
]

indicator_sets = {
    "std1" : [
    EMA(13),
    MACD(12, 26, 9)
    ],
    "std2" : [
    EMA(13),
    MACD(7, 36, 5)
    ]
}

def validate_date_param(date):
    return True

def validate_stock_param(stock):
    return True

def validate_ind_param(indicators):
    return True

def validate_set_param(set):
    return True

# Returns a list of Indicator objects
def parse_indicators(indicators):
    return indicator_sets["std1"]

def parse_sets(sets):
    if not isinstance(sets, list) or not isinstance(sets, str):
        raise TypeError("The parameter must be in the form of a string or a list of strings.")

    if isinstance(sets, list):
        for item in sets:
            if item not in indicator_sets:
                raise TypeError("One of the items passed through was not a proper indicator set.")

        # create list containing all elements in the sets mentioned
        list = []
        for set in sets:
            list.extend(indicators_sets[set])

        # remove duplicates
        temp = []
        for item in list:
            if item not in temp:
                temp.append(item)
        return temp
    else:

def parse_arguments(parser):
    if not isinstance(parser, argparse.ArgumentParser):
        raise TypeError("You must pass through a argparse.ArgumentParser object.")

    # set up string variables to represent the optional parameters' names
    indicators_option1, indicators_option2 = "-i", "--indicators"
    all_indicators_option = "--all_indicators"
    list_indicators_option = "--list_indicators"

    # indicator sets
    choose_set_option = "--set"
    list_indicator_sets_option = "--list_sets"

    # add arguments
    parser.add_argument(global_helpers.stock_option1, global_helpers.stock_option2, nargs="+", type=str, help=global_helpers.stock_param_help_msg)
    parser.add_argument(global_helpers.date_option1, global_helpers.date_option2, nargs="+", type=str, help=global_helpers.date_param_help_msg)

    parser.add_argument(indicators_option1, indicators_option2, nargs="+", type=str, help="Select what indicators to use")
    parser.add_argument(all_indicators_option, help="Calculate all indicators at once", action='store_true')
    parser.add_argument(list_indicators_option, help="Lists all indicators that can be passed through", action="store_true")

    parser.add_argument(choose_set_option, nargs="+", type=str, help="Choose an indicator set to use just this time")
    parser.add_argument(list_indicator_sets_option, help="Lists what indicator sets there are to choose from", action="store_true")
    return parser.parse_args()

def print_available_indicators():
    list_ind_msg = "The indicators available for use is as follows:"
    print(list_ind_msg)
    for item in helpers.all_indicators:
        print(" "*5 + item)
