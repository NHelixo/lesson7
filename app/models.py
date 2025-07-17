from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return self.name
    

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    rating = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"Оцінка: {self.rating}, Автор: {self.author}, Продукт {self.product}"
