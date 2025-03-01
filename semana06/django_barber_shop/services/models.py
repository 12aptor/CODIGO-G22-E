from django.db import models

class ServiceModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField()

    class Meta:
        db_table = 'services'


class BarberModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    speciality = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'barbers'

class ScheduleModel(models.Model):
    id = models.AutoField(primary_key=True)

    DAY_OF_WEEK_CHOICES = (
        ('MONDAY', 'MONDAY'),
        ('TUESDAY', 'TUESDAY'),
        ('WEDNESDAY', 'WEDNESDAY'),
        ('THURSDAY', 'THURSDAY'),
        ('FRIDAY', 'FRIDAY'),
        ('SATURDAY', 'SATURDAY'),
        ('SUNDAY', 'SUNDAY'),
    )

    day_of_week = models.CharField(choices=DAY_OF_WEEK_CHOICES, max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    barber = models.ForeignKey(
        BarberModel,
        on_delete=models.CASCADE,
        related_name='schedules',
        db_column='barber_id'
    )

    class Meta:
        db_table = 'schedules'