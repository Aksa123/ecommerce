from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from decimal import Decimal


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200, default=None)
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Console(models.Model):
    name = models.CharField(max_length=200)
    series = models.CharField(max_length=100, default=None)
    quantity = models.IntegerField(default=0)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, validators=[MinValueValidator(Decimal('0.01'))], help_text="Min is 0.00, and max is 999.99")
    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default=None)
    console = models.ManyToManyField(Console)
    quantity = models.IntegerField(default=0)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, default=None)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, validators=[MinValueValidator(Decimal('0.01'))], help_text="Min is 0.00, and max is 999.99")
    def __str__(self):
        return self.name

