from django.contrib import admin
from . import models
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'available', 'date_of_entry', 'rating', 'price')
    list_filter = ('title', 'writer', 'genre', 'available', 'rating', 'publishing_house')
    search_fields = ('title', 'writer', 'genre')
    ordering = ['title', 'quantity',]
admin.site.register(models.Book, BookAdmin)