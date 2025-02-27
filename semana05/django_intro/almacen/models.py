from django.db import models

class CategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    STATUS_CHOICES = (
        ('ACTIVE', 'ACTIVE'),
        ('INACTIVE', 'INACTIVE'),
        ('DELETED', 'DELETED'),
    )

    status = models.CharField(choices=STATUS_CHOICES, max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'categories'

class ProductModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        db_column='category_id',
        related_name='products'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'products'