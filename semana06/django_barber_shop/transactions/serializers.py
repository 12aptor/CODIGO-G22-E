from rest_framework import serializers
from .models import (
    CustomerModel,
    AppointmentModel,
)
from authentication.serializers import UserSerializer
from services.serializers import (
    BarberSerializer,
    ServiceSerializer,
)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = ("name", "email", "document_number", "address")

class AppointmentSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    user = UserSerializer(read_only=True)
    barber = BarberSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)

    class Meta:
        model = AppointmentModel
        fields = ("appointment_date", "user", "barber", "service", "customer")

    def create(self, validated_data):
        customer = validated_data.pop("customer")
        customer, _ = CustomerModel.objects.get_or_create(
            document_number=customer.get("document_number"),
            defaults=customer,
        )

        appointment = AppointmentModel.objects.create(
            customer=customer,
            **validated_data
        )

        return appointment
