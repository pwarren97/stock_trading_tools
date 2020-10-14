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
