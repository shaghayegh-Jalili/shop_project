from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {'products': products})


def store(request):
    return render(request, 'store.html')


def product(request):
    return render(request, 'product.html')


def checkout(request):
    return render(request, 'checkout.html')
