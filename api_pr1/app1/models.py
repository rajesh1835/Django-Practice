from django.db import models

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_id = models.PositiveIntegerField()

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category_name = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    pname = models.CharField(max_length=100)
    pid = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.pname
    