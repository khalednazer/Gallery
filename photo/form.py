from .models import Phot, Cat
from django.forms import ModelForm
from django import forms


class form(ModelForm):
    class Meta:
        model = Phot
        fields = '__all__'
        catg = forms.ModelChoiceField(
            queryset=Cat.objects.all(),
            widget=forms.Select(attrs={'class': 'form-select'}),
            empty_label="Select a category",
        )
