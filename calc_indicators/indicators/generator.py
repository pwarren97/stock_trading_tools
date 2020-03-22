from indicators.model import Indicator
from datetime import datetime

if conf.DB == "mongodb":
    from stt_global_items.dbms.mongodb import Mongo as dbms
elif conf.DB == "sql":
    from stt_global_items.dbms.sql import SQL as dbms

class IndicatorGenerator():
    def __init__(self, stock_df, indicator_set):
        err_msg = "Indicators must be passed through in the form of a list of indicators"
        if not isinstance(indicator_set, list):
            raise TypeError(err_msg)
        for item in indicator_set:
            if not isinstance(item, Indicator):
                raise TypeError(err_msg)
        # Sets the indicator set
        self.indicator_set = indicator_set

    def calc_indicators(self, start_date, end_date=None):
        if not isinstance(start_date, datetime):
            raise TypeError("The start date must be in the form of a python datetime.datetime object.")
        elif end_date is not None and not isinstance(end_date, datetime):
            raise TypeError("The end date must be in the form of a python datetime.datetime object.")

        self.indicator_df = dbms.get_indicators(start_date, end_date)
        return True
