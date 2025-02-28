from django.db import models

class CanchaModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=9)
    estado = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'canchas'

class ReservaModel(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    nombre_cliente = models.CharField(max_length=200)
    tiempo = models.IntegerField()
    cancha = models.ForeignKey(
        CanchaModel,
        on_delete=models.CASCADE,
        related_name='reservas',
        db_column='cancha_id' 
    )

    class Meta:
        db_table = 'reservas'