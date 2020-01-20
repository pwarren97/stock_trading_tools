# This file has helpers for __main__.py
from datetime import datetime, timedelta
import re

def validate_input(args):
    if args.date:
        # Check each date to make sure it has a valid format
        for item in args.date:
            if not re.search("^[0-9]{8}$", item):
                raise ValueError("You need a valid date in the format yyyymmdd")
    pass

def parse_dates(dates):
    year, month, day = parse_date(dates[0])
    start_date = datetime(year, month, day)

    if len(dates) == 2:
        year, month, day = parse_date(dates[1])
        end_date = datetime(year, month, day)
    elif len(dates) == 1:
        # makes end_date one day ahead of start_date
        end_date = start_date + timedelta(days=1)
    return (start_date, end_date)

def parse_date(date):
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])
    return (year, month, day)
