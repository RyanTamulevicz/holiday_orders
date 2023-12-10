from django.db import models


class Customer(models.Model):
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)


class Category(models.Model):
    category_name = models.CharField(max_length=200)


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    created = models.DateTimeField("date created")
    status = models.CharField(max_length=200)
    page_number = models.IntegerField(default=0)
    line_number = models.IntegerField(default=0)
