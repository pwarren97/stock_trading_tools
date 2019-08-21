from sources import iex

stock_data = iex.get_stock_data("AAPL", "20190101", "20190102")

print(stock_data)
