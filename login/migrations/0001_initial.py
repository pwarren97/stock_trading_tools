# Generated by Django 3.1.2 on 2020-10-18 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='datetime')),
                ('username', models.CharField(max_length=50, verbose_name='username')),
                ('success', models.BooleanField(verbose_name='success')),
                ('pass_attempted', models.CharField(max_length=256, verbose_name='pass_attempted')),
            ],
            options={
                'db_table': 'login_records',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='username')),
                ('password', models.CharField(max_length=256, verbose_name='password')),
                ('last_login', models.DateTimeField(max_length=200, verbose_name='last_login')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]