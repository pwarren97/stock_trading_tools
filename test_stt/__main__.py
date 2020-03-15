import unittest
from stt_global_items import conf
import pandas as pd
from datetime import datetime

if conf.DB == "mongodb":
    from stt_global_items.dbms.mongodb import Mongo as dbms
elif conf.DB == "sql":
    from stt_global_items.dbms.sql import SQL as dbms

class TestDBMS(unittest.TestCase):

    # data is the same pulled from IEXCloud
    def setUp(self):
        """Gets called before every test case"""
        # Single stock Multiple date example
        self.sing_stock_mult_date = {
            "date": [datetime(2019, 1, 2), datetime(2019, 1, 3), datetime(2019, 1, 4)],
            "symbol": ["AAPL", "AAPL", "AAPL"],
            "volume": [37039737.0, 91312195.0, 58607070.0],
            "high": [158.85, 145.72, 148.55],
            "low": [154.23, 142, 143.8],
            "close": [157.92, 142.19, 148.26],
            "open": [154.89, 143.98, 144.53]
        }
        # Single stock Single date example
        self.sing_stock_sing_date = {
            "date": [datetime(2019, 1, 2)],
            "symbol": ["AAPL"],
            "volume": [37039737.0],
            "high": [158.85],
            "low": [154.23],
            "close": [157.92],
            "open": [154.89]
        }
        # Multiple stock Multiple date example
        # self.mult_stock_mult_date = {
        #     "date": [datetime(2019, 1, 2), datetime(2019, 1, 3), datetime(2019, 1, 4), datetime(2019, 1, 2), datetime(2019, 1, 3), datetime(2019, 1, 4)],
        #     "symbol": ["AAPL", "AAPL", "AAPL", "MSFT", "MSFT", "MSFT"],
        #     "volume": [37039737.0, 91312195.0, 58607070.0],
        #     "high": [158.85, 145.72, 148.55],
        #     "low": [154.23, 142, 143.8],
        #     "close": [157.92, 142.19, 148.26],
        #     "open": [154.89, 143.98, 144.53]
        # }

        self.test_df1 = pd.DataFrame(self.sing_stock_mult_date)
        self.test_df2 = pd.DataFrame(self.sing_stock_sing_date)
        # self.test_df3 = pd.DataFrame(self.mult_stock_mult_date)

    def tearDown(self):
        """Gets called after every test case"""
        pass

    def test_save_stock_data(self):
        """Tests dbms.save_stock_data()"""
        dbms.save_stock_data(self.test_df1)

    def test_get_stock_data(self):
        """Tests dbms.get_stock_data()"""
        dbms.save_stock_data(self.test_df1)
        df1 = dbms.get_stock_data(["AAPL"], datetime(2019, 1, 2), datetime(2019, 1, 4))
        df2 = dbms.get_stock_data(["AAPL"], datetime(2019, 1, 2))

        self.assertTrue(self.test_df1.equals(df1['AAPL']))
        self.assertFalse(self.test_df1.equals(df2['AAPL']))

    def test_save_symbols(self):
        """Tests dbms.save_stock_data()"""
        pass

    def test_get_indicators(self):
        """Tests dbms.get_indicators()"""
        pass

    def test_save_indicators(self):
        """Tests dbms.save_indicators()"""
        pass


class TestSource(unittest.TestCase):
    def test_get_stock_data(self):
        """Tests source.get_stock_data()"""
        pass

unittest.main()
