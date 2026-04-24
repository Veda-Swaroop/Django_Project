from django.shortcuts import render

from .models import Product

# Create your views here.


def home(request):
    context = {"data": Product.objects.all()}
    return render(request, "store/home.html", context)


def about(request):
    return render(request, "store/about.html")


def contact(request):
    return render(request, "store/contact.html")


def products(request):
    context = {"data": Product.objects.all()}
    return render(request, "store/products.html", context)
