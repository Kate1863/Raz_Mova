from django.contrib import admin

# Register your models here.
from . import models

class CurrencyAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'description',
    ]

class WriterAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'description',
    ]

class GenreAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'genre',
        'description',
    ]

class SerieAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
    ]

class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'description',
    ]
admin.site.register(models.Currency, CurrencyAdmin)
admin.site.register(models.Writer, WriterAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Serie, SerieAdmin)
admin.site.register(models.PublishingHouse, PublishingHouseAdmin)
