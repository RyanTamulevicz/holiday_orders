# Register your models here.

from django.contrib import admin

from .models import Order, Customer, Category, Item

admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Item)
