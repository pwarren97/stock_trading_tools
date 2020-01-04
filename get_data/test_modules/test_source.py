import conf
import pandas as pd
from datetime import datetime

# Select your data source based on conf.py
if conf.DATA_SOURCE = "iex":
    from sources import iex as source

# Test with just a start_date
stocks = ["AAPL"]
start_date = datetime(2019, 01, 02)
stock_df = source.get_stock_data(stocks, start_date, close_only=True)

print("Result of source.get_stock_data() with a single stock and no end date")
if type(stock_df) == pd.DataFrame:
    if stock_df.columns == ["symbol", "date", "close", "volume"]:


# Test with an end_date as well
end_date = datetime(2019, 01, 02)
stock_df = source.get_stock_data(stocks, start_date, end_date, close_only=True)
