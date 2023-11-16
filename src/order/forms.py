from django import forms
from . import models
from catalog.models import Book
    



class OrderForm(forms.Form):
    user = forms.CharField(
        min_length=4,
        empty_value=False,
        required=True,
    )

    #product = forms.CharField(
        #name = forms.BookModelForm(forms.ModelForm)
    #)

    summ = forms.DecimalField(   
        max_digits=8,
        decimal_places=2,
    )                          
        
    order_currency = forms.CharField(
        max_length=3,
        empty_value=False,
    )

class OrderModelForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            'user',
            'summ',
            'order_currency',
        ]