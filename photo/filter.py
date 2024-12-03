from django import forms
from django_filters import  CharFilter, ModelMultipleChoiceFilter
from .models import Phot, Cat
from django_filters import FilterSet

class fil(FilterSet):
    category_filter = ModelMultipleChoiceFilter(queryset = Cat.objects.all(), 
    widget = forms.CheckboxSelectMultiple,
    label="Filter by Category"
    )
    class Meta:
        model = Phot
        fields= ['catg']
