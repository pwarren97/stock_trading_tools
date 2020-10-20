from django.db import models


user_len = 50
pass_len = 256 # size of sha3-256 hash for right now

# Create your models here.
class User(models.Model):
    username = models.CharField('username', max_length=user_len)
    password = models.CharField('password', max_length=pass_len)
    last_login = models.DateTimeField('last_login', max_length=200)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'

class LoginRecord(models.Model):
    datetime = models.DateTimeField('datetime')
    username = models.CharField('username', max_length=user_len)
    success = models.BooleanField('success')
    pass_attempted = models.CharField('pass_attempted', max_length=pass_len)

    def __str__(self):
        delimiter = "; "
        pass_fail = 'pass' if self.success else 'fail'
        return self.datetime + delimiter + self.username + delimiter + pass_fail

    class Meta:
        db_table = 'login_records'
