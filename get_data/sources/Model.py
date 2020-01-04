# This file serves as the template for future things

class Source():
    @staticmethod
    def get_stock_data(ticker_symbols, start, end=None, close_only=False):
        """
        Return pandas object with symbol, date, open, high, low, close, volume
        """
        raise NotImplementedError

    @staticmethod
    def get_symbols():
        """
        Return the symbols of the stock market in a pandas object
        """
        raise NotImplementedError
