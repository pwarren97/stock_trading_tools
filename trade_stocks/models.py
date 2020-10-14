from django.db import models

# Create your models here.
class Stocks(models.Model):
    date = models.DateTimeField('date')
    open = models.FloatField('open')
    high = models.FloatField('high')
    low = models.FloatField('low')
    close = models.FloatField('close')
    volume = models.FloatField('volume')
    source = models.CharField('source', max_length=200)

    class Meta:
        db_table = 'historical_stock_data'

class Symbols(models.Model):
    date = models.DateTimeField('date_pulled')
    symbol = models.CharField('symbol', max_length=200)
    name = models.CharField('name', max_length=200)
    exchange = models.CharField('exchange', max_length=200)
    currency = models.CharField('currency', max_length=200)
    region = models.CharField('region', max_length=200)
    source = models.CharField('source', max_length=200)
    type = models.CharField('type', max_length=200) # prefered stock, common stock as ps, cs

    class Meta:
        db_table = 'symbols'
