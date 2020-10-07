# This file has helpers for __main__.py
from datetime import datetime
import re

def validate_input(args):
    if args.date:
        # Check each date to make sure it has a valid format
        for item in args.date:
            if not re.search("^[0-9]{8}$", item):
                raise ValueError("You need a valid date in the format yyyymmdd")
    pass
