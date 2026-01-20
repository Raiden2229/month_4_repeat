from django.db import models


class Products(models.Model):
    name_products = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    description = models.TextField
