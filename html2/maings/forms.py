from django import forms
from maings.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name','description','price',
        )