from django.shortcuts import render

# Create your views here.


dummy_data = [
    {
        "item_name": "Product 1",
        "category": "abcd",
        "price": "20,000 Rupees",
        "description": "samsung company smartphone",
    },
    {
        "item_name": "Product 2",
        "category": "abdhy",
        "price": "80,000 Rupees",
        "description": "Apple company smartphone",
    },
    {
        "item_name": "Product 3",
        "category": "andh",
        "price": "50,000 Rupees",
        "description": "Google company smartphone",
    },
]


def home(request):
    context = {"data": dummy_data}
    return render(request, "store/home.html", context)


def about(request):
    return render(request, "store/about.html")


def contact(request):
    return render(request, "store/contact.html")


def products(request):
    context = {"data": dummy_data}
    return render(request, "store/products.html", context)
