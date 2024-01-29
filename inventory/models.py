from django.db import models

# Create your models here.
class Stock(models.Model):
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category_id = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    available = models.IntegerField(default=0)
    mrp_price = models.DecimalField(max_digits=6, decimal_places=2)

class Sale(models.Model):
    key = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    product_id = models.IntegerField
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    sell_price = models.DecimalField(max_digits=6, decimal_places=2)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)

class IncomingStock(models.Model):
    key = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    product_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    mrp_price = models.DecimalField(max_digits=6, decimal_places=2)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
