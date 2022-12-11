from django.shortcuts import render
from .models import Product

def index(request):
    template_name = 'index.html'
    products = Product
    context = {
        'products': products
    }
    return render(request, template_name, context)
