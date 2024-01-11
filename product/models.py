from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    has_sizes = models.BooleanField(default=True, null=True, blank=True)
    colour = models.CharField(max_length=30, default='not specified')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)
    
    @property
    def has_sizes(self):
        return self.size != ''
    
    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
