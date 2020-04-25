from .model import Indicator
import stt_global_items.conf as conf
import pandas as pd

if conf.DB == "mongodb":
    from stt_global_items.dbms.mongodb import Mongo as dbms
elif conf.DB == "sql":
    from stt_global_items.dbms.sql import SQL as dbms


class EMA(Indicator):
    # days represents the day window, e.g. 7 days means a 7-day EMA
    def __init__(self, days):
        self.days = days

    def calc_indicator(data_frame):
        pass

    def __eq__(self, obj):
        if notisinstance(obj, EMA):
            return False
        elif self.days == obj.days:
            return True
        else:
            return False

    def __ne__(self, obj):
        return not self.__eq__(obj)
