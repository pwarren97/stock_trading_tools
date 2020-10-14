# Generated by Django 3.1.2 on 2020-10-14 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, verbose_name='username')),
                ('password', models.CharField(max_length=200, verbose_name='password')),
                ('last_login', models.DateTimeField(max_length=200, verbose_name='last_login')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
