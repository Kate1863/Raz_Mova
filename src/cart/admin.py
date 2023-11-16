from django.contrib import admin
from . import models
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = [
        'customer',
        'created'
    ]

class ProductInCartAdmin(admin.ModelAdmin):
    list_display=[
        'cart',
        'product',
        'quantity',
        'price',
    ]

admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.ProductInCart, ProductInCartAdmin)