from django.forms import TextInput

from .models import Car
from django import forms

class CarForm(forms.ModelForm):
    class Meta:
        """Формы для заполнения в БД данных об авто"""
        model = Car
        fields = ('name', 'model_name', 'year', 'country')





