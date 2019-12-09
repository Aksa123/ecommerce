# Generated by Django 2.2.7 on 2019-12-05 13:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(default='normal user', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2019, 12, 5, 13, 48, 57, 792312, tzinfo=utc)),
        ),
    ]
