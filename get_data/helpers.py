# This file has helpers for __main__.py
from datetime import datetime, timedelta

def validate_input(args):
    pass

def get_start_and_end_dates(dates):
    year = int(dates[0][:4])
    month = int(dates[0][4:6])
    day = int(dates[0][6:])
    start_date = datetime(year, month, day)

    if len(dates) == 2:
        year = int(dates[1][:4])
        month = int(dates[1][4:6])
        day = int(dates[1][6:])
        end_date = datetime(year, month, day)
    elif len(dates) == 1:
        # makes end_date one day ahead of start_date
        end_date = start_date + timedelta(days=1)
    return (start_date, end_date)
