from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class IceCream(models.Model):
    FLAVOR_CHOICES = [
        ('vanilla', 'Vanilla'),
        ('chocolate', 'Chocolate'),
        ('strawberry', 'Strawberry'),
    ]

    flavor = models.CharField(max_length=100, choices=FLAVOR_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_vegan = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.flavor} Ice Cream"
