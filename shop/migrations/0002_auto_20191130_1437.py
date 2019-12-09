# Generated by Django 2.2.7 on 2019-11-30 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='console',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.Console'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='country',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='console',
            name='series',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='maker',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.Manufacturer'),
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.Genre'),
        ),
    ]