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
        if not isinstance(data_frame, pd.DataFrame):
            raise TypeError("The pandas object must be a pandas dataframe")

        # TODO: Should check to make sure the pandas object is in the proper format

        # Store the data row by row
        for idx in range(len(data_frame)):
            data_frame.iloc[idx]
            row = data_frame.iloc[idx].to_dict()
            # Update is used here instead of insert too avoid duplicates
            db.stocks.update_one(row, { "$set": row }, upsert=True)

    @staticmethod
    def get_stock_data(ticker_symbols, dates):
        if not isinstance(dates, tuple):
            raise TypeError("Dates must be in the form of a tuple containing the start and end (exclusive of the end date)")
        elif not isinstance(ticker_symbols, list):
            raise TypeError("Ticker_symbols must be passed in the form a list")
        # elif all(isinstance(item, str) for item in ticker_symbols):
        #     raise TypeError("Items in the ticker_symbols list must be strings")
        elif not isinstance(dates[0], datetime):
            raise TypeError("Dates passed through must be datetime.datetime objects inside of a tuple")
        elif not isinstance(dates[1], datetime):
            raise TypeError("Dates passed through must be datetime.datetime objects inside of a tuple")
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
        print(data_frame.columns)
        #TODO: Should check to make sure the pandas object is in the proper format

        # save the symbols now row by row
        for idx in range(len(data_frame)):
            row = data_frame.loc[idx].to_dict()
            # Update is used here instead of inse
            db.symbols.update(row, { "$set" : row }, upsert=True)
