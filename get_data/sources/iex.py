from iexfinance.stocks import get_historical_data
import conf

# return stock data in pandas database
# date open high low close volume
def get_stock_data(ticker_symbol, start, end):
    # Force all the types to be appropriate
    if not isinstance(ticker_symbol, str):
        raise TypeError("ticker_symbol must be a string.")
    elif not isinstance(start, str):
        raise TypeError("start must be a string.")
    elif not isinstance(end, str):
        raise TypeError("end must be a string.")

    # Get the data from online
    stock_data = get_historical_data(ticker_symbol, start, end, output_format='pandas', token=iex_token)
    return stock_data
