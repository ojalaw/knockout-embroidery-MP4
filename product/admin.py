from django.contrib import admin
from .models import Product, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'colour', 'price', 'size', 'stock', 'available')
    list_filter = ('available', 'size', 'colour')
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock', 'available')


admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
