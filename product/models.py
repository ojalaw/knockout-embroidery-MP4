from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=10)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product_images')
    
    def __str__(self):
        return self.name
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
