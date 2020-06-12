from datetime import datetime

# Single stock Multiple date example
sing_stock_mult_date = {
    "date": [datetime(2019, 1, 2), datetime(2019, 1, 3), datetime(2019, 1, 4)],
    "symbol": ["AAPL", "AAPL", "AAPL"],
    "volume": [37039737.0, 91312195.0, 58607070.0],
    "high": [158.85, 145.72, 148.55],
    "low": [154.23, 142, 143.8],
    "close": [157.92, 142.19, 148.26],
    "open": [154.89, 143.98, 144.53]
}
# Single stock Single date example
sing_stock_sing_date = {
    "date": [datetime(2019, 1, 2)],
    "symbol": ["AAPL"],
    "volume": [37039737.0],
    "high": [158.85],
    "low": [154.23],
    "close": [157.92],
    "open": [154.89]
}
# Multiple stock Multiple date example
mult_stock_mult_date = {
    "date": [datetime(2019, 1, 2), datetime(2019, 1, 3), datetime(2019, 1, 4), datetime(2019, 1, 2), datetime(2019, 1, 3), datetime(2019, 1, 4)],
    "symbol": ["AAPL", "AAPL", "AAPL", "MSFT", "MSFT", "MSFT"],
    "volume": [37039737.0, 91312195.0, 58607070.0, 35329345.0, 42578410.0, 44060620.0],
    "high": [158.85, 145.72, 148.55, 101.75, 100.19, 102.51],
    "low": [154.23, 142, 143.8, 98.94, 97.2, 98.93],
    "close": [157.92, 142.19, 148.26, 101.12, 97.4, 101.93],
    "open": [154.89, 143.98, 144.53, 99.55, 100.1, 99.72]
}
# Multiple stock Single date example
mult_stock_sing_date = {
    "date": [datetime(2019, 1, 2), datetime(2019, 1, 2)],
    "symbol": ["AAPL", "MSFT"],
    "volume": [37039737.0, 35329345.0],
    "high": [158.85, 101.75],
    "low": [154.23, 98.94],
    "close": [157.92, 101.12],
    "open": [154.89, 99.55]
}

symbols = {
    "cik": ["1090872", "1675149", None, None],
    "currency": ["USD", "USD", "USD", "USD"],
    "date": ["2020-03-19", "2020-03-19", "2020-03-19", "2020-03-19"],
    "exchange": ["NYS", "NYS", "PSE", "NAS"],
    "figi": ["BBG000C2V3D6", "BBG00B3T3HD3", "BBG00LPXX872", "BBG000V2S3P6"],
    "name": ["Agilent Technologies Inc.", "Alcoa Corp.", "Perth Mint Physical Gold ETF", "ATA Creativity Global Sponsored ADR"],
    "region": ["US", "US", "US", "US"],
    "symbol": ["A", "AA", "AAAU", "AACG"],
    "type": ["cs", "cs", "et", "ad"],
    "source": ["iex", "iex", "iex", "iex"]
}
