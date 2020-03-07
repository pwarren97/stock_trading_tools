
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
symbol,    date,    indicators : [ EMA : [13, 200], MACD : [12-26-9: [ Signal-line, MACD_line, MACD_histogram ], SRoC: [13-7], RoC: [7]  ]
