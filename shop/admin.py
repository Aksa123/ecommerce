from django.contrib import admin
from .models import Manufacturer, Genre, Console, Game

# Register your models here.

class ManufacturerAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.name

class GenreAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.name

class ConsoleAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.name

class GameAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.name

admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Console, ConsoleAdmin)
admin.site.register(Game, GameAdmin)