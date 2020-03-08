import unittest
from stt_global_items import conf
import pandas as pd
from datetime import datetime


class TestDBMS(unittest.TestCase):

    def setUp(self):
        """Gets called before every test case"""
        if conf.DB == "mongodb":
            from stt_global_items.dbms.mongodb import Mongo as dbms
        elif conf.DB == "sql":
            from stt_global_items.dbms.sql import SQL as dbms

    def tearDown(self):
        """Gets called after every test case"""
        pass

    def test_save_stock_data(self):
        """Tests dbms.save_stock_data()"""
        data = {
            "date": [datetime(2019, 1, 2), datetime(2019, 1, 3), datetime(2019, 1, 4)],
            "symbol": ["AAPL", "AAPL", "AAPL"],
            "volume": [37039737, 91312195, 58607070],
            "high": [158.85, 145.72, 148.55],
            "low": [154.23, 142, 143.8],
            "close": [157.92, 142.19, 148.26],
            "open": [154.89, 143.98, 144.53]
        }
        stock_df = pd.DataFrame(data)
        dbms.save_stock_data(stock_df)

    def test_get_stock_data(self):
        """Tests dbms.get_stock_data()"""
        data = {
            "date": [datetime(2019, 1, 2), datetime(2019, 1, 3), datetime(2019, 1, 4)],
            "symbol": ["AAPL", "AAPL", "AAPL"],
            "volume": [37039737, 91312195, 58607070],
            "high": [158.85, 145.72, 148.55],
            "low": [154.23, 142, 143.8],
            "close": [157.92, 142.19, 148.26],
            "open": [154.89, 143.98, 144.53]
        }
        stock_df = pd.DataFrame(data)
        dbms.save_stock_data(stock_df)
        new_df = dbms.get_stock_data(["AAPL"], datetime(2019, 01, 03))
        self.assertEqual(stock_df, new_df)

    def test_save_symbols(self):
        """Tests dbms.save_stock_data()"""
        pass

    def test_get_indicators(self):
        """Tests dbms.get_indicators()"""
        pass

    def test_save_indicators(self):
        """Tests dbms.save_indicators()"""
        pass

    def run(self, result=None):
        self.test_save_stock_data()
        self.test_get_stock_data()
