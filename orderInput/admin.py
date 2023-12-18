# Register your models here.

from django.contrib import admin

from .models import Order, Customer, Item

admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Item)
