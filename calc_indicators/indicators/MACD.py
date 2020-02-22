from Model import Indicator

class MACD(Indicator):
    # EMA's are to be used for the MACD and Signal Line
    def __init__(self, EMA1, EMA2, EMA3):
        self.EMA1 = EMA1
        self.EMA2 = EMA2
        self.EMA3 = EMA3

    def calc_indicator(ticker_symbols, start, end=None):
        pass
