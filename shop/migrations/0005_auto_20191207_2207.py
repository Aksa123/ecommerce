# Generated by Django 3.0 on 2019-12-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20191207_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='console',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
        migrations.AddField(
            model_name='game',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
    ]
