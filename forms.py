from django import forms
from .models import Product, IceCream

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']  

class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = ['flavor', 'price', 'is_vegan']
