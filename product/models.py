from django.db import models
from django.contrib.auth.models import User
from django.utils.timesince import timesince
from django.utils import timezone

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
    
    EMBROIDERY_LOCATIONS = (
        ('UL', 'Upper Left'),
        ('LL', 'Lower Left'),
        ('C', 'Centre'),
        ('UR', 'Upper Right'),
        ('LR', 'Lower Right'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    sku = models.CharField(max_length=100, null=True, blank=True)
    colour = models.CharField(max_length=30, choices=COLOUR_CHOICES, default='not specified')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='M')
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)
    embroidery_location = models.CharField(max_length=2, choices=EMBROIDERY_LOCATIONS, default='C', null=True, blank=True)
    embroidery_text = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='Review Title')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title} by {self.user.username}'

    def timesince_posted(self):
        return timesince(self.date_posted)