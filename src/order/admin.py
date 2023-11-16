from django.contrib import admin

# Register your models here.
from . import models

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'user',
        'summ',
        'order_currency',
    ]

admin.site.register(models.Order, OrderAdmin)

