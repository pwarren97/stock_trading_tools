from django.db import models

# Create your models here.
class Stocks(models.Model):
    date = models.DateTimeField('date')
    open = models.Float('open', 52)
    high = models.Float('high', 52)
    low = models.Float('low', 52)
    close = models.Float('close', 52)
    volume = models.Float('volume', 52)
    source = CharField('source', max_length=200)
