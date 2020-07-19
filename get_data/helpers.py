# This file has helpers for __main__.py
from datetime import datetime
import re

def import_download_source():
    if conf.DATA_SOURCE == "iex":
        from sources.iex import IEXCloud as source
    # elif conf.DATA_SOURCE == "someotherone":
    #     from sources.iex import ThatObject as source
    return source

def validate_input(args):
    if args.date:
        # Check each date to make sure it has a valid format
        for item in args.date:
            if not re.search("^[0-9]{8}$", item):
                return False
    else:
        return False
    return True
