from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField( max_length = 255)
    description = models.TextField()
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField( max_length = 200)

    image = models.CharField( max_length = 300)
    # Why? Because most websites store images on different servers
    # and store only urls on main site

    def __str__(self):
        return f'{self.name}'

class Order(models.Model):
    # Each order is comprise of set of items in it and the details 
    # the user who ordered it.
    order_contents = models.CharField( max_length = 1000, null = True)
    price = models.FloatField( null = True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    created_at = models.DateTimeField( auto_now_add = True)

    def __str__(self):
        return f"Order by {self.first_name} {self.last_name} {self.created_at}"
