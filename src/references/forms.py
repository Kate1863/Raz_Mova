from django import forms
from django.core.exceptions import ValidationError
from . import models

def my_validator(field):
    if field == "xxx":
        raise ValidationError ("It can`t be 'xxx'")


class CurrencyForm(forms.Form):
    name = forms.CharField(
        max_length= 3,
        required=True,
        empty_value="BYN",
        label="Currency name:",
        help_text="Please, enter currency name in ISO3",
        validators=[my_validator],
        )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea()
    )

    def save_obj(self):
        name = self.cleaned_data.get("name")
        description = self.cleaned_data.get("description")
        obj = models.Currency.objects.create(name=name, description=description)
        return obj
    
    def update_obj(self, pk):
        name = self.cleaned_data.get("name")
        description = self.cleaned_data.get("description")
        models.Currency.objects.filter(pk=pk).update(name=name, description=description)

class CurrencyModelForm(forms.ModelForm):
    class Meta:
        model = models.Currency
        fields = [
            'name',
            'description'
        ]

class WriterModelForm(forms.ModelForm):
    class Meta:
        model = models.Writer
        fields = ("name", "description")


class GenreModelForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = ("genre", "description")


class SerieModelForm(forms.ModelForm):
    class Meta:
        model = models.Serie
        fields = ('name',)


class PublishingHouseModelForm(forms.ModelForm):
    class Meta:
        model = models.PublishingHouse
        fields = ("name", "description")