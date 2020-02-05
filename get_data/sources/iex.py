from iexfinance.stocks import get_historical_data
import iexfinance.refdata
import conf
import pandas as pd
from Model import Source
from datetime import datetime, timedelta

# DB
# database information gets used to check what data to use from the database
if conf.DB == "mongodb":
    from dbms.mongodb import Mongo as dbms
elif conf.DB == "sql":
    from dbms.sql import SQL as dbms

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

        # Check if data is in the database
        # Returns a dict of all the stock data
        if end == None:
            end = start

        if close_only:
            stock_data = pd.DataFrame(columns=["symbol", "date", "close", "volume"])
        else:
            stock_data = pd.DataFrame(columns=["symbol", "date", "open", "high", "low", "close", "volume"])


        for ticker_symbol in ticker_symbols:
            # Check to see what data is already in the database
            ticker_symbol = ticker_symbol.upper()
            db_data = dbms.get_stock_data([ticker_symbol], start, end)[ticker_symbol]

            # get just the dates that matter
            if close_only == True:
                db_data = db_data["date"]
            if close_only == False:
                db_data = db_data.loc[pd.isna(db_data["high"]) != True, "date"]
            print(db_data)

            # Create a range of dates not in the db to pull
            date_range = (start, end)
            db_data_pointer = db_data[0]
            db_data_end = db_data[len(db_data)-1]
            date_counter = start # date is the counter here
            while date_counter != end:
                while db_data_pointer != db_data_end:
                # if the date is in the database
                for item in db_data:
                    if date_counter == item.to_pydatetime():
                        date_range[1] = date_counter - timedelta(days=1)
                        # Pull data
                        temp = get_historical_data(ticker_symbol, date_range[0], date_range[1], output_format='pandas', token=conf.IEX_TOKEN, close_only=close_only)
                        # Eliminate IEXCloud specific information for db
                        temp = restructure_df(temp, ticker_symbol, close_only)
                        stock_data = pd.concat([stock_data, temp], ignore_index=True)


                # Pull data
                temp = get_historical_data(ticker_symbol, date_range[0], date_range[1], output_format='pandas', token=conf.IEX_TOKEN, close_only=close_only)
                # Eliminate IEXCloud specific information for db
                temp = restructure_df(temp, ticker_symbol, close_only)
                stock_data = pd.concat([stock_data, temp], ignore_index=True)

                date_counter = date_counter + timedelta(days=1)
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
