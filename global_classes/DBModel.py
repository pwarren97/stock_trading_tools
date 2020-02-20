from ABC import abc, abstractmethod

class DBModel(abc):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_stock_data(ticker_symbols, start, end=None):
        pass
