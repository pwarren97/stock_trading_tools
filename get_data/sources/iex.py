from iexfinance.stocks import get_historical_data
import iexfinance.refdata
import stt_global_items.conf as conf
import pandas as pd
from .model import Source
from datetime import datetime, timedelta

# DB
# database information gets used to check what data to use from the database
if conf.DB == "mongodb":
    from stt_global_items.dbms.mongodb import Mongo as dbms
elif conf.DB == "sql":
    from stt_global_items.dbms.sql import SQL as dbms

class IEXCloud(Source):
    """
    Class representing the connection to the IEXCloud platform.
    It inherits from the Source class in template.py,
    <get_data.sources.Model.Source>.

    functions:
    get_stocks_data(ticker_symbol, start, end=None, close_only=False)
    get_symbols()
    """
    @staticmethod
    def get_stock_data(ticker_symbols, start, end=None, close_only=False):

        # Force all the types to be appropriate
        if not isinstance(ticker_symbols, list):
            raise TypeError("ticker_symbol must be a list.")
        elif not isinstance(start, datetime):
            raise TypeError("start must be a datetime.date object.")
        elif not isinstance(end, datetime) and not end == None:
            raise TypeError("end must be a datetime.date object.")

        for item in ticker_symbols:
            if not isinstance(item, str):
                raise TypeError("An item in ticker_symbol is not a string.")

        if not end == None and not start < end:
            raise ValueError("The start needs to come before the end.")

        if close_only:
            stock_data = pd.DataFrame(columns=["symbol", "date", "close", "volume"])
        else:
            stock_data = pd.DataFrame(columns=["symbol", "date", "open", "high", "low", "close", "volume"])


        # if no end is specified
        if end == None:
            there_is_only_one_date_listed = True
        else:
            there_is_only_one_date_listed = False

        for ticker_symbol in ticker_symbols:
            # Check to see what data is already in the database
            ticker_symbol = ticker_symbol.upper()
            db_data = dbms.get_stock_data([ticker_symbol], start, end)[ticker_symbol]

            if there_is_only_one_date_listed:
                # only do something if it didn't find the date stored in the db
                if len(db_data) == 0:
                    stock_data = pull_then_add_data(stock_data, ticker_symbol, start, start, close_only)
            else:
                if len(db_data) != 0:
                    # keep only the dates that matter
                    if close_only == True:
                        db_data = db_data["date"]
                    if close_only == False:
                        db_data = db_data.loc[pd.isna(db_data["high"]) != True, "date"]
                    db_data = [ date.to_pydatetime() for date in db_data ]

                    # Create a range of dates not in the db represent the range that you end up pulling
                    date_range = [start, end]
                    db_data_loc = 0
                    db_data_end = len(db_data)-1
                    date_pointer = start # date_pointer is acting as a counter here

                    while date_pointer < end:
                        if date_pointer == db_data[db_data_loc]:
                            date_range[1] = date_pointer - timedelta(days=1)
                            # Pull data, then add it to the stock_data dataframe
                            stock_data = pull_then_add_data(stock_data, ticker_symbol, date_range[0], date_range[1], close_only)

                            # Fastforward the db_data_loc to be past a range of consecutive dates in db_data if that is what it is looking at
                            while db_data_loc < db_data_end and db_data[db_data_loc+1] == db_data[db_data_loc] + timedelta(days=1):   # Stops at the last consecutive date
                                db_data_loc = db_data_loc + 1

                            date_pointer = db_data[db_data_loc] + timedelta(days=1)
                            date_range[0] = date_pointer
                            if db_data_loc < db_data_end:
                                db_data_loc = db_data_loc + 1

                        date_pointer = date_pointer + timedelta(days=1)
                    if date_pointer == end:
                        date_range[1] = date_pointer
                        # Pull data, then add it to the stock_data dataframe
                        stock_data = pull_then_add_data(stock_data, ticker_symbol, date_range[0], date_range[1], close_only)
                else:
                    # Pull data
                    stock_data = pull_then_add_data(stock_data, ticker_symbol, start, end, close_only)
        return stock_data


    @staticmethod
    def get_symbols():
        symbols = iexfinance.refdata.get_symbols(output_format='pandas', token=conf.IEX_TOKEN)

        # Remove IEX specific info
        del symbols["iexId"]
        del symbols["isEnabled"]

        return symbols

# Eliminate IEXCloud specific information for putting data in the database
def restructure_df(data_frame, ticker_symbol, close_only):
    data_frame['date'] = data_frame.index
    data_frame.index.name = None
    data_frame.index = range(len(data_frame))
    data_frame['symbol'] = ticker_symbol
    if close_only:
        data_frame = data_frame[["symbol", "date", "close", "volume"]]
    else:
        data_frame = data_frame[["symbol", "date", "open", "high", "low", "close", "volume"]]
    return data_frame

def pull_then_add_data(stock_df, ticker_symbol, start, end, close_only):
    temp = get_historical_data(ticker_symbol, start, end, output_format='pandas', token=conf.IEX_TOKEN, close_only=close_only)
    temp = restructure_df(temp, ticker_symbol, close_only)
    return pd.concat([stock_df, temp], ignore_index=True)
