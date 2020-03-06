
# Table/Collections:
## Symbols
SQL:
id(primary key), currency, date, exchange, name, region, symbol, type

Mongo:
currency, date, exchange, name, region, symbol, type

## Stock Prices
SQL:
id(foreign key),    symbol,   date,    open,   high,    low,    close,   volume

Mongo:
symbol, date, open, high, low, close, volume

## Indicators
SQL:
id(foreign key),    symbol,   date,    13-EMA,   MACD,    Signal_line   MACD_histogram, Mtm7, S-RoC 13/21

Mongo:
id,   symbol,    date,    indicators : [13-EMA, [ MACD, Signal_line ], MACD_histogram, Mtm7,  S-RoC 13/21]
