from Model import Model
import pymongo

class Mongo(Model):
    """
    Class for communicating with a MongoDB.

    Contains functions:
    save_stock_data()
    """

    def __init__():
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["stocks"]

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
        if not isinstance(data_frames, list):
            raise TypeError("The pandas objects must be in a list")

        # TODO: Should check to make sure the pandas object is in the proper format

        # Store the data row by row
        for data_frame in data_frames:
            for idx in range(len(data_frame)):
                row = data_frame.loc[idx].to_json()
                db.stocks.insert_one(row)

    @staticmethod
    def save_symbols(data_frame):
        """
        Saves symbols to the database.
        """
        if not isinstance(data_frame, list):
            raise TypeError("The pandas objects must be in a list")

        #TODO: Should check to make sure the pandas object is in the proper format

        # get rid of the symbols not being used
        del symbols["Id"]
        del symbols["iexId"]
        del symbols["isEnabled"]

        # save the symbols now row by row
        for idx in range(len(data_frame)):
            row = data_frame.loc[idx].to_json()
            db.symbols.insert_one(row)
