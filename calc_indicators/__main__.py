import argparse
import conf
from datetime import datetime, timedelta
import helpers

if conf.DB == "mongodb":
    from dbms.mongodb import Mongo as dbms

# Parse the command line input
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--stock", nargs="+", type=str, help="")
parser.add_argument("-d", "--date", nargs="+", type=str, help="")
parser.add_argument("-i", "--indicator", nargs="+", type=str, help="")
args = parser.parse_args()

if args.date:
    start_date, end_date = helpers.parse_start_and_end_dates(args.date)
df = dbms.get_stock_data(args.stock, start_date, end_date)
print("Data looks as follows:")
for ticker in df:
    print(df[ticker])
