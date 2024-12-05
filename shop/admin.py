from django.contrib import admin
from .models import Product
# Register your models here.
from .models import Order

admin.site.register(Product)
admin.site.register(Order)

