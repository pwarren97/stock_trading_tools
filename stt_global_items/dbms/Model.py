# This file will represent all models

class DBMS_Model:
    @staticmethod
    def save_stock_data(data_frame):
        """
        Saves a list of pandas objects to the database with columns:

        symbol      date        open    high    low     close      volume
        -------------------------------------------------------------------
        AAPL        20190102    154.89  158.85  154.23  157.92     37039737
        AAPL        20190103    143.98  145.72  142.0   142.19     91312195
        AAPL        20190104    144.53  148.54  143.8   148.26     58607070
        AAPL        20190107    148.7   148.83  145.9   147.93     54777764

        OR (if only close prices):

        symbol      date        close      volume
        -------------------------------------------
        AAPL        20190102    157.92     37039737
        AAPL        20190103    142.19     91312195
        AAPL        20190104    148.26     58607070
        AAPL        20190107    147.93     54777764
        """
        raise NotImplementedError

    @staticmethod
    def get_stock_data(ticker_symbols, start, end=None):
        """
        returns pandas.DataFrame object corresponding to ticker symbols and dates
        get_stock_date(ticker_symbols, dates)

        Data must be in the form:
        ticker_symbols = [string, string, ...]
        dates = (string, string)


        if get_stock_data(["AAPL"], (20190102, 20190107)) is called, the DataFrame returned:
        symbol      date        open    high    low     close      volume
        -------------------------------------------------------------------
        AAPL        20190102    154.89  158.85  154.23  157.92     37039737
        AAPL        20190103    143.98  145.72  142.0   142.19     91312195
        AAPL        20190104    144.53  148.54  143.8   148.26     58607070
        AAPL        20190107    148.7   148.83  145.9   147.93     54777764

        Or, if open, high, and low are missing in some places:
        symbol      date        open    high    low     close      volume
        -------------------------------------------------------------------
        AAPL        20190102    154.89  158.85  154.23  157.92     37039737
        AAPL        20190103    143.98  145.72  142.0   142.19     91312195
        AAPL        20190104    144.53  148.54  143.8   148.26     58607070
        AAPL        20190107    148.7   148.83  145.9   147.93     54777764
        """
        raise NotImplementedError

    @staticmethod
    def save_symbols(data_frame):
        """
        Saves symbols to the database. Must be in a pandas object.
        """
        raise NotImplementedError

    @staticmethod
    def get_indicators(indicators, start, end=None):
        raise NotImplementedError

    @staticmethod
    def save_indicators(data_frame):
        raise NotImplementedError
