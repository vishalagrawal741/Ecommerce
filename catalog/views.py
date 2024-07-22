from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse

def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/index.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/index2.html', {'product': product})

def home(request):
    return HttpResponse('Hello, World!')
