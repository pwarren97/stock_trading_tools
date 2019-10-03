from iexfinance.stocks import get_historical_data
import iexfinance.refdata
import conf
import pandas as pd
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

        # If an end date is specified
        if end == None:
            data_frame = get_historical_data(ticker_symbol, start, output_format='pandas', token=conf.IEX_TOKEN, close_only=True)

        elif int(start) < int(end):
            data_frame =  get_historical_data(ticker_symbol, start, end, output_format='pandas', token=conf.IEX_TOKEN, close_only=True)
        else:
            # if the start date is in the wrong place but hasn't
            # been handled correctly by __main__.py
            raise ValueError("The start needs to come before the end.")

        # Add extra information to the table
        data_frame['date'] = data_frame.index
        data_frame['symbol'] = ticker_symbol[0].upper()
        return data_frame

    @staticmethod
    def get_symbols():
        """
        Returns all the symbols
        """
        symbols = iexfinance.refdata.get_symbols(output_format='pandas', token=conf.IEX_TOKEN)

        # Remove IEX specific info
        print(symbols.columns)
        del symbols["iexId"]
        del symbols["isEnabled"]

        return symbols
