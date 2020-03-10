# This file serves as the template for future things

class Source(): # not inheriting abc because it doesn't give a NotImplementedError
    @staticmethod
    def get_stock_data(ticker_symbols, start, end=None, close_only=False):
        """
        Returns historical stock data in a list of pandas objects.
        Parameters must be in the form of strings.
        Ticker symbol does not have to be case sensitive, but it does have to be a list
        ***The end date is intended to be inclusive

        Returns columns: symbol date open high low close volume

        For close_only: symbol date close volume
        """
        raise NotImplementedError

    @staticmethod
    def get_symbols():
        """
        Returns all the symbols
        """
        raise NotImplementedError
