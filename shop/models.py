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
