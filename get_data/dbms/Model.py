# This file will represent all models

class Model:
    @staticmethod
    def save_stock_data(data_frames):
        """
        Saves a list of pandas objects to the database with columns:

        symbol      date        open    high    low     close      volume
        -------------------------------------------------------------------
        AAPL        20190102    154.89  158.85  154.23  157.92     37039737
        AAPL        20190103    143.98  145.72  142.0   142.19     91312195
        AAPL        20190104    144.53  148.54  143.8   148.26     58607070
        AAPL        20190107    148.7   148.83  145.9   147.93     54777764
        """
        pass

    @staticmethod
    def get_stock_data(dates):
        pass

    @staticmethod
    def save_symbols(data_frame):
        pass
