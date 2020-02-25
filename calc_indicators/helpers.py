# This file has helpers for __main__.py
from datetime import datetime

indicator_names = \
[
"MACD:12-26-9",
"MACD-Histogram:12-26-9"
]

def parse_start_and_end_dates(dates):
    year, month, day = parse_date(dates[0])
    start_date = datetime(year, month, day)

    if len(dates) == 2:
        year, month, day = parse_date(dates[1])
        end_date = datetime(year, month, day)
    elif len(dates) == 1:
        # makes end_date one day ahead of start_date
        end_date = None
    return (start_date, end_date)

# return a datetime object from a date string passed through
def parse_date(date):
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])
    return (year, month, day)

def calc_indicators(indicators, start_date, end_date=None):
    if not isinstance(indicators, list):
        raise TypeError("The indicators must be passed in the from of a list.")
    elif not isinstance(indicators[0], str):
        raise TypeError("The indicators must be in the form of a string.")
    elif not isinstance(start_date, datetime):
        raise TypeError("The start date must be in the form of a python datetime.datetime object.")
    elif end_date is not None:
        if not isinstance(end_date, datetime):
            raise TypeError("The end date must be in the form of a python datetime.datetime object.")
