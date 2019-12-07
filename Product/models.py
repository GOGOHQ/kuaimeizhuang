from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=15)


class Brand(models.Model):
    name = models.CharField(max_length=15)
    ename = models.CharField(max_length=15)


class Product(models.Model):
    name = models.CharField(max_length=15)
    category = models.ForeignKey("Category",on_delete=models.CASCADE)
    picUrl = models.CharField(max_length=150)
    sketch = models.TextField(max_length=40)
    colorspecies = models.ManyToManyField("Colorspecies")
    brand = models.ForeignKey("Brand",on_delete=models.CASCADE)


class Colorspecies(models.Model):
    name = models.CharField(max_length=15)
    r = models.IntegerField(validators=[
        MaxValueValidator(255),
        MinValueValidator(0)
    ])
    g = models.IntegerField(validators=[
        MaxValueValidator(255),
        MinValueValidator(0)
    ])
    b = models.IntegerField(validators=[
        MaxValueValidator(255),
        MinValueValidator(0)
    ])




