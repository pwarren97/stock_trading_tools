from Model import Model
import pymongo
import conf
from datetime import datetime
import pandas as pd

client = pymongo.MongoClient(conf.MONGO_SOCKET)
db = client["stocks"]

class Mongo(Model):
    """
    Class for communicating with a MongoDB.
    """

    @staticmethod
    def get_stock_data(ticker_symbols, start, end=None):
        """
        Data pulled in data frame containing all stock information and listed in order by date
        """
        if not isinstance(start, datetime):
            raise TypeError("The start date must be in the form of a datetime object")
        elif not isinstance(ticker_symbols, list):
            raise TypeError("Ticker_symbols must be passed in the form a list")
        # elif all(isinstance(item, str) for item in ticker_symbols):
        #     raise TypeError("Items in the ticker_symbols list must be strings")
        if end==None:
            end = start
        else:
            if not isinstance(end, datetime):
                raise TypeError("The end date must be in the form of a datetime object")

        results = {}
        for ticker_symbol in ticker_symbols:
            # cursor pulls data when you want to access it, such as in a for loop
            # data will go away after a full iteration in a for loop
            ticker_symbol = ticker_symbol.upper()
            cursor = db.stocks.find({ "symbol" : ticker_symbol, "date": {"$gte" : start, "$lte" : end} }).sort([("date", pymongo.ASCENDING)])

            appropriate_cols = ["symbol", "date", "open", "high", "low", "close", "volume"]
            results[ticker_symbol] = pd.DataFrame(columns=appropriate_cols)
            for item in cursor:
                db_data = pd.DataFrame(item, index=[0])
                del db_data['_id']
                results[ticker_symbol] = pd.concat([results[ticker_symbol], db_data], ignore_index=True, sort=True)
        return results
