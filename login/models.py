from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField('username', max_length=200)
    password = models.CharField('password', max_length=200)
    last_login = models.DateTimeField('last_login', max_length=200)

    class Meta:
        db_table = 'users'
