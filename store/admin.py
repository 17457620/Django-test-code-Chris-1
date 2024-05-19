from django.contrib import admin
from .models import Category, Employee, Product, Order

admin.site.register(Category)
admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(Order)
