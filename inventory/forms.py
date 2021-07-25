from django import forms
from django.forms import fields

from .models import * 

class MenuCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = '__all__' 

class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
