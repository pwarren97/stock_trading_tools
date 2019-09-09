import Model
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
    def save_stock_data(pandas_obj):
        """
        Saves a list of pandas objects to the database with columns:
        symbol, date, open, high, low, close
        """
        if not isinstance(pandas_obj, list):
            raise TypeError("The pandas object must be in a list")
