from iexfinance.stocks import get_historical_data
import iexfinance.refdata
import conf
import pandas as pd
from template import Source
from datetime import datetime

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
    <get_data.sources.template.Source>.

    functions:
    get_stocks_data(ticker_symbol, start, end=None, close_only=False)
    get_symbols()
    """
    @staticmethod
    def get_stock_data(ticker_symbols, start, end=None, close_only=False):
        """
        Returns historical stock data in a list of pandas objects.
        Parameters must be in the form of strings.
        Ticker symbol does not have to be case sensitive, but it does have to be a list

        Returns columns: date open high low close volume symbol
        """
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

        if end==None:
            end = datetime(start.year, start.month, start.day)

        if not start < end:
            raise ValueError("The start needs to come before the end.")

        # Check if data is in the database
        pd_obj = dbms.get_stock_data(ticker_symbols, (start, end))

        data_frames = []

        # If an end date is specified
        if end == None:
            for ticker_symbol in ticker_symbols:
                # Pull data
                data_frame = get_historical_data(ticker_symbol, start, output_format='pandas', token=conf.IEX_TOKEN, close_only=close_only)

                # Restructure the data to have the appropriate format
                restructure_df(data_frame, ticker_symbol)
                data_frame.append(data_frame)
        # If end and start date is specified and is correct
        elif start < end:
            for ticker_symbol in ticker_symbols:
                # Pull data
                data_frame = get_historical_data(ticker_symbol, start, end, output_format='pandas', token=conf.IEX_TOKEN, close_only=close_only)

                # Restructure the data to have the appropriate format
                restructure_df(data_frame, ticker_symbol)
                data_frame.append(data_frame)
        else:
            # if the start date is in the wrong place but hasn't
            # been handled correctly by __main__.py
            raise ValueError("The start needs to come before the end.")

<<<<<<< HEAD
        if len(ticker_symbol) > 1 and stock_data != None:

        return stock_data
=======
        return data_frames
>>>>>>> be5b868a1e6fc7499a52c4ea4d909e63b57193b0

    @staticmethod
    def get_symbols():
        """
        Returns all the symbols
        """
        symbols = iexfinance.refdata.get_symbols(output_format='pandas', token=conf.IEX_TOKEN)

        # Remove IEX specific info
        del symbols["iexId"]
        del symbols["isEnabled"]

        return symbols

# Makes data frame format correct for IEXCloud
# This function is just for use in this file, not to be supplied elsewhere
def restructure_df(data_frame, ticker_symbol):
    data_frame['date'] = data_frame.index
    data_frame.index.name = None
    data_frame.index = range(len(data_frame))
    data_frame['symbol'] = ticker_symbol.upper()
    return data_frame
