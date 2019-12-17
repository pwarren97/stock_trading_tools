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
            end = datetime(start.year, start.month, start.day+1)

        if not start < end:
            raise ValueError("The start needs to come before the end.")

        # Check if data is in the database
        # pd_obj_dict = dbms.get_stock_data(ticker_symbols, (start, end))

        if close_only:
            data = pd.DataFrame(columns=["date", "close", "volume", "symbol"])
        else:
            data = pd.DataFrame(columns=["date", "open", "high", "low", "close", "volume", "symbol"])

        for ticker_symbol in ticker_symbols:
            # Pull data
            temp = get_historical_data(ticker_symbol, start, end, output_format='pandas', token=conf.IEX_TOKEN, close_only=close_only)
            # Restructure the data to have the appropriate format
            temp = restructure_df(temp, ticker_symbol)
            data = data.append(temp, sort=True)
        return data

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
