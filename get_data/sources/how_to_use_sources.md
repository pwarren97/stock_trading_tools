# Interface for all future download utilities

## To get the symbols for populating the database
### Should only need to be used once
- get_symbols()

## To get stock data for a specific stock
- get_stock_data(ticker_symbol, start, end=None)
- return pandas object with open, high, low, close, volume

## To get stock data for several stocks
- get_stock_data([ticker_symbol1, ticker_symbol2, ...], start, end=start)
- return for each stock open, high, low, close, volume
