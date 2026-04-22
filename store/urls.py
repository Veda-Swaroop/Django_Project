from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="store-home"),
    path("about/", views.about, name="store-about"),
    path("contact/", views.contact, name="store-contact"),
    path("products/", views.products, name="store-products"),
]
