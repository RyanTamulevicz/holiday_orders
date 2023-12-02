from django.db import models


class Customer(models.Model):
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created = models.DateTimeField("date created")
    status = models.CharField(max_length=200)
    page_number = models.IntegerField(default=0)
    line_number = models.IntegerField(default=0)


class Category(models.Model):
    category_name = models.CharField(max_length=200)


class Item(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
