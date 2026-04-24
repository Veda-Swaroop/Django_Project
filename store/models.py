from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30, unique=True, default="Undefined")
    price = models.IntegerField(default=0)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
