# Import necessary modules
from django import forms
from .models import Product

# Define the ProductForm form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price')
        labels = {
            'name': 'Product Name',
            'description': 'Product Description',
            'price': 'Product Price'
            
        }
