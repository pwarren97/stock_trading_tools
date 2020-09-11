import unittest
from stt_global_items import conf
import pandas as pd
from datetime import datetime
import numpy as np
from test_stt.db_model_tests import sample_data


from stt_global_items.dbms.mongodb import Mongo as dbms

class TestDBMS(unittest.TestCase):

    # data is the same pulled from IEXCloud
    # Note: Volume has to be a float, it errors with an integer, must see if there is an integer fix
    def setUp(self):
        """Gets called before every test case"""
        self.test_df1 = pd.DataFrame(sample_data.sing_stock_mult_date)
        self.test_df2 = pd.DataFrame(sample_data.sing_stock_sing_date)
        self.test_df3 = pd.DataFrame(sample_data.mult_stock_mult_date)
        self.test_df4 = pd.DataFrame(sample_data.mult_stock_sing_date)

        self.test_symbols = pd.DataFrame(sample_data.symbols)

    def tearDown(self):
        """Gets called after every test case"""
        pass

    def test_save_stock_data(self):
        """Tests dbms.save_stock_data()"""
        pass

    def test_get_stock_data(self):
        """Tests dbms.get_stock_data()"""
        # data was saved in the test_save_stock_data() test,
        # failures from test_save_stock_data() might cause errors in this function
        df1 = dbms.get_stock_data(["AAPL"], datetime(2019, 1, 2), datetime(2019, 1, 4))
        df1 = df1["AAPL"]

        df2 = dbms.get_stock_data(["AAPL"], datetime(2019, 1, 2))

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

    def test_save_symbols(self):
        """Tests dbms.save_symbols()"""
        dbms.save_symbols(self.test_symbols)

    def test_get_symbols(self):
        """Tests dbms.get_symbols()"""
        # all = dbms.get_symbols()
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
