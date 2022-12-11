from django.db import models
from maings.conf import *

class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.IntegerField(default=0)
    currency = models.CharField(max_length=120, choices=CURRENCY)