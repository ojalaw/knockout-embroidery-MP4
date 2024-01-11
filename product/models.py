from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    SIZE_CHOICES = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'X-Large'),
        ('XXL', 'XX-Large'),
    )
    COLOUR_CHOICES = (
        ('Black', 'Black'),
        ('White', 'White'),
        ('Grey', 'Grey'),
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Yellow', 'Yellow'),
        ('Green', 'Green'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    colour = models.CharField(max_length=30, choices=COLOUR_CHOICES, default='not specified')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='M')
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()