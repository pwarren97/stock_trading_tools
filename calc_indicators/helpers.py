# This file has helpers for __main__.py
import pandas as pd
from datetime import datetime
# from indicators.model import Indicator
# from indicator_sets import IndicatorSet

all_indicators = \
[
"EMA",
"MACD",
"RoC",
"SRoC"
]

indicator_sets = {
    "std1" :
    [
        # Indicators
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


class IndicatorGenerator():
    def __init__(stock_df, indicator_set):
        if not isinstance(indicator_set, IndicatorSet):
            raise TypeError("The indicator set passed through must be of type IndicatorSet")
        self.indicator_set = indicator_set

    def calc_indicators(start_date, end_date=None):
        if not isinstance(start_date, datetime):
            raise TypeError("The start date must be in the form of a python datetime.datetime object.")
        elif end_date is not None and not isinstance(end_date, datetime):
            raise TypeError("The end date must be in the form of a python datetime.datetime object.")

        return True
