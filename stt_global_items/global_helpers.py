from datetime import datetime

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

# Optional parameters for the CLI
stock_option1, stock_option2 = "-s", "--stock"
date_option1, date_option2 = "-d", "--date"

# Components of the cli output
help_msg = "Use -h or --help to see the options."

# Help messages for argparse
stock_param_help_msg = "what stock(s) to download. input should be ticker symbols"
date_param_help_msg = "takes start date or start and end dates for stock data in format yyyymmdd"
