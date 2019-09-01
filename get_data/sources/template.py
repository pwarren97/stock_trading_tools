# This file serves as the template for future things

class Source():
    @staticmethod
    def get_stock_data(ticker_symbol, start, end=None):
        """
        Return pandas object with open, high, low, close, volume
        """
        raise NotImplementedError

    @staticmethod
    def get_symbols():
        raise NotImplementedError
