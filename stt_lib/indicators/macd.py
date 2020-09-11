from .model import Indicator
import stt_lib.conf as conf
from stt_lib.dbms.helpers import import_dbms
from .ema import EMA

dbms = import_dbms()

# Outputs MACD line, Signal Line, and the MACD-Histogram
class MACD(Indicator):
    # EMA's are to be used for the MACD and Signal Line
    def __init__(self, ema1, ema2, ema3):
        if not isinstance(ema1, int) or not isinstance(ema2, int) or not isinstance(ema3, int):
            raise TypeError("You must pass all parameters in the form of an integer.")
        self.ema1 = EMA(ema1)
        self.ema2 = EMA(ema2)
        self.ema3 = EMA(ema3)

    # Returns the MACD line, the Signal Line, and the Histogram
    def calc_indicator(data_frame):
        pass

    def __eq__(self, obj):
        if not isinstance(obj, MACD):
            return False
        elif self.ema1 == obj.ema1 and self.ema2 == obj.ema2 and self.ema3 == self.ema3:
            return True
        else:
            return False

    def __ne__(self, obj):
        return not self.__eq__(obj)
