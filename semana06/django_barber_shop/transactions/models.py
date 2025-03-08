from django.db import models
from authentication.models import UserModel
from services.models import BarberModel, ServiceModel


class CustomerModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    document_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    class Meta:
        db_table = "customers"


class AppointmentModel(models.Model):
    id = models.AutoField(primary_key=True)
    appointment_date = models.DateTimeField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="appointments",
        db_column="user_id",
    )
    barber = models.ForeignKey(
        BarberModel,
        on_delete=models.CASCADE,
        related_name="appointments",
        db_column="barber_id",
    )
    service = models.ForeignKey(
        ServiceModel,
        on_delete=models.CASCADE,
        related_name="appointments",
        db_column="service_id",
    )
    customer = models.ForeignKey(
        CustomerModel,
        on_delete=models.CASCADE,
        related_name="appointments",
        db_column="customer_id",
    )

    class Meta:
        db_table = "appointments"


class PaymentModel(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField()

    PAYMENT_METHOD_CHOICES = (
        ("CASH", "CASH"),
        ("CARD", "CARD"),
        ("YAPE", "YAPE"),
        ("PLIN", "PLIN"),
    )

    payment_method = models.CharField(choices=PAYMENT_METHOD_CHOICES, max_length=10)
    payment_date = models.DateTimeField()
    appointment = models.ForeignKey(
        AppointmentModel,
        on_delete=models.CASCADE,
        related_name="payments",
        db_column="appointment_id",
    )

    class Meta:
        db_table = "payments"
