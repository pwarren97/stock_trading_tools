# Generated by Django 3.1.2 on 2020-10-15 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20201014_1853'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.AlterModelTable(
            name='loginrecord',
            table='login_records',
        ),
    ]
