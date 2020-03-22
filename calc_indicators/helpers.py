# This file has helpers for __main__.py
import pandas as pd
from datetime import datetime
from indicators.model import Indicator
from indicators.ema import EMA
from indicators.macd import MACD

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
