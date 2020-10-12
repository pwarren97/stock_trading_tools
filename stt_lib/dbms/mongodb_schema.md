# Schema for MongoDB model
db:
  stocks

collections:
  stocks
  symbols
  indicators

stocks entry:
  {
    open,
    high,
    low,
    close,
    volume,
    source
  }

symbols entry:
{
  symbol,
  date,
  open,
  high,
  low,
  close,
  volume
}

indicators:
{
  
}