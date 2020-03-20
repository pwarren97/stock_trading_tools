# This file has helpers for __main__.py
import pandas as pd
from datetime import datetime
from indicators.model import Indicator


all_indicators = \
[
"EMA:13",
"EMA:200",
"MACD:12-26-9", #MACD does histogram as well
"RoC:7",
"SRoC:13-7"
]

class IndicatorGenerator():
    def __init__(indicators):
        if not isinstance(indicators, list):
            raise TypeError("The indicators must be passed in the from of a list.")
        elif not isinstance(indicators[0], str):
            raise TypeError("The indicators must be in the form of a string.")
        self.indicators = indicators

    def calc_indicators(start_date, end_date=None):
        if not isinstance(start_date, datetime):
            raise TypeError("The start date must be in the form of a python datetime.datetime object.")
        elif end_date is not None:
            if not isinstance(end_date, datetime):
                raise TypeError("The end date must be in the form of a python datetime.datetime object.")
        return True
