from Model import Model
import pandas as pd
import pymongo
from datetime import datetime
import conf

# global db information used by all the functions
client = pymongo.MongoClient(conf.MONGO_SOCKET)
db = client["stocks"]

class Mongo(Model):
    """
    Class for communicating with a MongoDB.

    Contains functions:
    save_stock_data()
    """

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
        if not isinstance(data_frame, pd.DataFrame):
            raise TypeError("The pandas object must be a pandas dataframe")

        # TODO: Should check to make sure the pandas object is in the proper format

        # Store the data row by row
        print("Data saved to the database looks as follows:")
        print(data_frame)
        for idx in range(len(data_frame)):
            data_frame.iloc[idx]
            row = data_frame.iloc[idx].to_dict()
            # Update is used here instead of insert too avoid duplicates
            db.stocks.update_one(row, { "$set": row }, upsert=True)
        print("\n")

    @staticmethod
    def get_stock_data(ticker_symbols, dates):
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

        if not isinstance(dates, tuple):
            raise TypeError("Dates must be in the form of a tuple containing the start and end (exclusive of the end date)")
        elif not isinstance(ticker_symbols, list):
            raise TypeError("Ticker_symbols must be passed in the form a list")
        # elif all(isinstance(item, str) for item in ticker_symbols):
        #     raise TypeError("Items in the ticker_symbols list must be strings")
        elif not isinstance(dates[0], datetime):
            raise TypeError("Dates passed through must be datetime.date inside of a tuple")
        elif not isinstance(dates[1], datetime):
            raise TypeError("Dates passed through must be datetime.date inside of a tuple")
        # elif not dates[0] < dates[1]:
        #     raise TypeError("Start date must be less than end date")

        results = {}
        for ticker_symbol in ticker_symbols:
            # cursor pulls data when you want to access it, such as in a for loop
            # data will go away after a full iteration in a for loop
            cursor = db.stocks.find({ "symbol" : ticker_symbol, "date": {"$gte" : dates[0], "$lte" : dates[1]} })

            results[ticker_symbol] = pd.DataFrame()
            for item in cursor:
                results[ticker_symbol] = results[ticker_symbol].append(item, ignore_index=True)
        return results

    @staticmethod
    def save_symbols(data_frame):
        """
        Saves symbols to the database. Must be in a pandas object.
        """
        print(data_frame.columns)
        #TODO: Should check to make sure the pandas object is in the proper format

        # save the symbols now row by row
        for idx in range(len(data_frame)):
            row = data_frame.loc[idx].to_dict()
            # Update is used here instead of inse
            db.symbols.update(row, { "$set" : row }, upsert=True)
