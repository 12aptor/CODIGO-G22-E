from django.db import models

class CategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Nombre')

    STATUS_CHOICES = (
        ('ACTIVE', 'ACTIVE'),
        ('INACTIVE', 'INACTIVE'),
        ('DELETED', 'DELETED'),
    )

    status = models.CharField(choices=STATUS_CHOICES, max_length=10, verbose_name='Estado')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'categories'
        verbose_name = 'Categoria de productos'
        verbose_name_plural = 'Categorias de productos'

class ProductModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Nombre')
    price = models.FloatField(verbose_name='Precio')
    status = models.BooleanField(default=True, verbose_name='Estado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado en')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado en')
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        db_column='category_id',
        related_name='products',
        verbose_name='Categoria'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'products'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'