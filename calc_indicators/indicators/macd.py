from .model import Indicator
import stt_global_items.conf as conf

if conf.DB == "mongodb":
    from stt_global_items.dbms import Mongo as dbms
elif conf.DB == "sql":
    from stt_global_items.dbms import SQL as dbms

# Outputs MACD line, Signal Line, and the MACD-Histogram
class MACD(Indicator):
    # EMA's are to be used for the MACD and Signal Line
    def __init__(self, ema1, ema2, ema3):
        self.EMA1 = EMA1
        self.EMA2 = EMA2
        self.EMA3 = EMA3

    # Returns the MACD line, the Signal Line, and the Histogram
    def calc_indicator(data_frame):
        pass