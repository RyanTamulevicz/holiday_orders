from django.db import models
from django.utils import timezone


class Customer(models.Model):
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)


class Category(models.Model):
    category_name = models.CharField(max_length=200)


class Order(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=False)
    created = models.DateTimeField("date created", default=timezone.now())
    status = models.CharField(max_length=200)


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    page_number = models.IntegerField(default=0)
    line_number = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)

    def save(self, *args, **kwargs):
        if not self.order_id:
            raise ValueError("An Item must be associated with an Order.")
        super().save(*args, **kwargs)
