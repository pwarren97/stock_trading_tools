from .model import DBMS_Model
import pandas as pd
import pymongo
from datetime import datetime
from stt_lib import conf

# global db to be used by all functions, since there is only one instance
db = None

class Mongo(DBMS_Model):
    """
    Class for communicating with a MongoDB.
    """
    @staticmethod
    def connect(host=None, port=None):
        """
        Connect to mongodb database
        """
        global db
        if host is None and port is None:
            client = pymongo.MongoClient(conf.MONGO_HOST, conf.MONGO_PORT)
        elif host is not None and port is not None:
            client = pymongo.MongoClient(host, port)
        else:
            raise ValueError('You need to specify either the host and port \
                number or specify nothing and it will use the default \
                configuration')

        db = client["stocks"]

    @staticmethod
    def use_sandbox(db_path=None):
        """
        Switches to using a sandbox for unit testing purposes.
        """
        global db
        try:
            # Start and then connect to the mongobox
            from mongobox import MongoBox
            box = MongoBox(db_path=db_path) if db_path != None else MongoBox()
            box.start()
            client = box.client()
            db = client['stocks']
        except:
            raise Exception("Could not connect to mongobox sandbox")

    @staticmethod
    def save_stock_data(data_frame):
        if not isinstance(data_frame, pd.DataFrame):
            raise TypeError("The pandas object must be a pandas dataframe")

        # TODO: Should check to make sure data_frame is in the proper format

        # Store the data row by row
        for idx in range(len(data_frame)):
            data_frame.iloc[idx]
            row = data_frame.iloc[idx].to_dict()

            # Update with upsert is used here instead of insert too avoid duplicates
            row_to_update = { "date" : row["date"], "symbol" : row["symbol"]}
            db.stocks.update_one(row_to_update, { "$set": row }, upsert=True)

    @staticmethod
    def get_stock_data(ticker_symbols, start, end=None):
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

        # for saving cleaned db output
        results = {}
        for ticker_symbol in ticker_symbols:
            # cursor pulls data when you want to access it, such as in a for loop
            # the cursor deletes data after a full iteration in a for loop
            ticker_symbol = ticker_symbol.upper()
            cursor = db.stocks.find({ "symbol" : ticker_symbol, "date": {"$gte" : start, "$lte" : end} }).sort([("date", pymongo.ASCENDING)])

            # Establish the columns we are going to use for the results data frame
            # This also deletes the old results dataframe for the last ticker_symbol, saving memory
            appropriate_cols = ["symbol", "date", "open", "high", "low", "close", "volume"]
            results[ticker_symbol] = pd.DataFrame(columns=appropriate_cols)

            # Add data to the results dataframe a row at a time
            for item in cursor:
                db_data = pd.DataFrame(item, index=[0])
                del db_data['_id']
                results[ticker_symbol] = pd.concat([results[ticker_symbol], db_data], ignore_index=True, sort=True)
        return results

    @staticmethod
    def save_symbols(data_frame):
        # save the symbols now row by row
        for idx in range(len(data_frame)):
            row = data_frame.loc[idx].to_dict()
            # Upsert makes it update and insert
            db.symbols.update_one(row, { "$set" : row }, upsert=True)

    @staticmethod
    def get_indicators(ticker_symbols, start, end=None):
        pass

    @staticmethod
    def save_indicators(data_frame):
        pass
