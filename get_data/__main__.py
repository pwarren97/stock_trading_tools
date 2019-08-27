from os import sys
import argparse

from sources import iex

# Get the historical stock data from the internet
stock_data = None
if len(sys.argv) == 2:
    # sys.argv[1] == ticker symbol name
    stock_data = iex.get_stock_data(sys.argv[1], "20190101", "20190102")
elif len(sys.argv) == 3:
    stock_data = iex.get_stock_data(sys.argv[1], sys.argv[2])


# if stock_data.any():
print(stock_data)
