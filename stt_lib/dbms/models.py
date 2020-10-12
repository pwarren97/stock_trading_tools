from django.db import models

class Stocks(models.Model):
    open = models.Float(52)
    high = models.Float(52)
    low = models.Float(52)
    close = models.Float(52)
    volume = models.Float(52)
    source = CharField(max_length=200)

class 