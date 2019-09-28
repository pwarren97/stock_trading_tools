from iexfinance.stocks import get_historical_data
import iexfinance.refdata
import conf
from template import Source

"""
This module covers iextrading based communication.

functions:
get_stock_data(ticker_symbol, start, end=None)
get_symbols()
"""
class IEXCloud(Source):
    """
    Class representing the connection to IEXCloud
    """
    @staticmethod
    def get_stock_data(ticker_symbol, start, end=None):
        """
        Returns historical stock data in a pandas object.
        Parameters must be in the form of strings.
        Ticker symbol does not have to be case sensitive, but it does have to be a list

        Returns columns: date open high low close volume
        """
        # Force all the types to be appropriate
        if not isinstance(ticker_symbol, list):
            raise TypeError("ticker_symbol must be a list.")
        elif not isinstance(start, str):
            raise TypeError("start must be a string.")
        elif not isinstance(end, str) and not end == None:
            raise TypeError("end must be a string.")

        for item in ticker_symbol:
            if not isinstance(item, str):
                raise TypeError("An item in ticker_symbol is not a string.")

        # Get the data from online
        if end == None:
            return get_historical_data(ticker_symbol, start, output_format='pandas', token=conf.IEX_TOKEN)
        elif int(start) < int(end):
            return get_historical_data(ticker_symbol, start, end, output_format='pandas', token=conf.IEX_TOKEN)
        else:
            # if the start date is in the wrong place but hasn't
            # been handled correctly by __main__.py
            raise ValueError("The start needs to come before the end.")
        return stock_data

    @staticmethod
    def get_symbols():
        """
        Returns all the symbols
        """
        symbols = iexfinance.refdata.get_symbols()

        # Remove IEX specific info
        del symbols["Id"]
        del symbols["iexId"]
        del symbols["isEnabled"]
        del symbols["currency"]

        return symbols
