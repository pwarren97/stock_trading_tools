from .model import Indicator
import stt_global_items.conf as conf
from .ema import EMA

if conf.DB == "mongodb":
    from stt_global_items.dbms import Mongo as dbms
elif conf.DB == "sql":
    from stt_global_items.dbms import SQL as dbms

# Outputs MACD line, Signal Line, and the MACD-Histogram
class MACD(Indicator):
    # EMA's are to be used for the MACD and Signal Line
    def __init__(self, ema1, ema2, ema3):
        self.ema1 = EMA(ema1)
        self.ema2 = EMA(ema2)
        self.ema3 = EMA(ema3)

    # Returns the MACD line, the Signal Line, and the Histogram
    def calc_indicator(data_frame):
        pass
