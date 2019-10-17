from dbms.mongodb import Mongo as dbms
import pandas as pd
import datetime
"""
Coverage:

"""
def run():
    # set data
    dates = [ datetime.datetime(2019, 01, 02),
              datetime.datetime(2019, 01, 03),
              datetime.datetime(2019, 01, 04),
              datetime.datetime(2019, 01, 07) ]

    df = pd.DataFrame({"symbol": ["AAPL", "AAPL", "AAPL", "AAPL"],
                       "date": dates,
                       "open": [ 154.89, 143.98, 144.53, 148.7 ],
                       "high": [ 158.85, 145.72, 148.54, 148.83 ],
                       "low": [ 154.23, 142.0, 143.8, 145.9 ],
                       "close": [ 157.92, 142.19, 148.26, 147.93 ],
                       "volume": [ 37039737, 91312195, 58607070, 54777764 ]})

    dbms.save_stock_data([df])

    # Get data
    result = dbms.get_stock_data(["AAPL"], ("20190102", "20190107"))
    print(result)
