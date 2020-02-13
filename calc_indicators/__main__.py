import argparse
import conf
from datetime import datetime, timedelta

if conf.DB == "mongodb":
    from dbms.mongodb import Mongo as dbms

# Parse the command line input
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--stock", nargs="+", type=str, help="")
parser.add_argument("-d", "--date", nargs="+", type=str, help="")
parser.add_argument("-i", "--indicator", nargs="+", type=str, help="")
args = parser.parse_args()
