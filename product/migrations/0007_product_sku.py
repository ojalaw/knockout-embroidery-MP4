# Generated by Django 5.0 on 2024-01-18 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_size_alter_product_colour'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(default='not specified', max_length=100, unique=True),
        ),
    ]
