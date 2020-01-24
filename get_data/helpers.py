# This file has helpers for __main__.py
from datetime import datetime
import re

def validate_input(args):
    if args.date:
        # Check each date to make sure it has a valid format
        for item in args.date:
            if not re.search("^[0-9]{8}$", item):
                raise ValueError("You need a valid date in the format yyyymmdd")
    pass

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
