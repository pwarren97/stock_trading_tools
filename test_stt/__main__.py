import unittest
from stt_global_items import conf
import pandas as pd
from datetime import datetime
import numpy as np

if conf.DB == "mongodb":
    from stt_global_items.dbms.mongodb import Mongo as dbms
elif conf.DB == "sql":
    from stt_global_items.dbms.sql import SQL as dbms

class TestDBMS(unittest.TestCase):

    # data is the same pulled from IEXCloud
    # Note: Volume has to be a float, it errors with an integer, must see if there is an integer fix
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
        self.mult_stock_mult_date = {
            "date": [datetime(2019, 1, 2), datetime(2019, 1, 3), datetime(2019, 1, 4), datetime(2019, 1, 2), datetime(2019, 1, 3), datetime(2019, 1, 4)],
            "symbol": ["AAPL", "AAPL", "AAPL", "MSFT", "MSFT", "MSFT"],
            "volume": [37039737.0, 91312195.0, 58607070.0, 35329345.0, 42578410.0, 44060620.0],
            "high": [158.85, 145.72, 148.55, 101.75, 100.19, 102.51],
            "low": [154.23, 142, 143.8, 98.94, 97.2, 98.93],
<<<<<<< HEAD
            "close": [157.92, 142.19, 148.26, 101.12, 97.4, 98.93],
            "open": [154.89, 143.98, 144.53, 99.55, 100.1, 99.72]
        }

=======
            "close": [157.92, 142.19, 148.26, 101.12, 97.4, 101.93],
            "open": [154.89, 143.98, 144.53, 99.55, 100.1, 99.72]
        }
        # Multiple stock Single date example
        self.mult_stock_sing_date = {
            "date": [datetime(2019, 1, 2), datetime(2019, 1, 2)],
            "symbol": ["AAPL", "MSFT"],
            "volume": [37039737.0, 35329345.0],
            "high": [158.85, 101.75],
            "low": [154.23, 98.94],
            "close": [157.92, 101.12],
            "open": [154.89, 99.55]
        }
>>>>>>> tests

        self.test_df1 = pd.DataFrame(self.sing_stock_mult_date)
        self.test_df2 = pd.DataFrame(self.sing_stock_sing_date)
        self.test_df3 = pd.DataFrame(self.mult_stock_mult_date)
<<<<<<< HEAD
=======
        self.test_df4 = pd.DataFrame(self.mult_stock_sing_date)
>>>>>>> tests

    def tearDown(self):
        """Gets called after every test case"""
        pass

    def test_save_stock_data(self):
        """Tests dbms.save_stock_data()"""
        dbms.save_stock_data(self.test_df1)
        dbms.save_stock_data(self.test_df2)
        dbms.save_stock_data(self.test_df3)
        dbms.save_stock_data(self.test_df4)

    def test_get_stock_data(self):
        """Tests dbms.get_stock_data()"""
        dbms.save_stock_data(self.test_df1)
        df1 = dbms.get_stock_data(["AAPL"], datetime(2019, 1, 2), datetime(2019, 1, 4))
        df1 = df1["AAPL"]

        df2 = dbms.get_stock_data(["AAPL"], datetime(2019, 1, 2))
<<<<<<< HEAD
        df3 = dbms.get_stock_data(["AAPL", "MSFT"], datetime(2019, 1, 2), datetime(2019, 1, 4))
        df3 = pd.concat([df3["AAPL"], df3["MSFT"]], ignore_index=True)


        print(self.test_df3["volume"].equals(df3["volume"]))



        self.assertTrue(self.test_df1.equals(df1['AAPL']))
        self.assertFalse(self.test_df1.equals(df2['AAPL']))
        self.assertTrue(self.test_df3.equals(df3))
=======
        df2 = df2["AAPL"]

        df3 = dbms.get_stock_data(["AAPL", "MSFT"], datetime(2019, 1, 2), datetime(2019, 1, 4))
        df3 = pd.concat([df3["AAPL"], df3["MSFT"]], ignore_index=True)

        df4 = dbms.get_stock_data(["AAPL", "MSFT"], datetime(2019, 1, 2))
        df4 = pd.concat([df4["AAPL"], df4["MSFT"]], ignore_index=True)
        # pd.concat made the dtype of the volume column np.int64 and it should be np.float64 to match with the other dfs,
        # that is why the following line has to be there
        df3["volume"] = np.array(df3["volume"], dtype=np.float64)
        df4["volume"] = np.array(df4["volume"], dtype=np.float64)

        # assert tests
        self.assertTrue(self.test_df1.equals(df1))
        self.assertFalse(self.test_df1.equals(df2))
        self.assertTrue(self.test_df3.equals(df3))
        self.assertTrue(self.test_df4.equals(df4))
>>>>>>> tests

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
