from rest_framework import serializers
from .models import (
    CustomerModel,
    AppointmentModel,
)
from services.serializers import (
    BarberSerializer,
    ServiceSerializer,
)
from authentication.models import UserModel
from services.models import BarberModel, ServiceModel

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = ("name", "email", "document_number", "address")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("name", "email", "role")

class AppointmentSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = AppointmentModel
        fields = ("appointment_date", "user", "barber", "service", "customer")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data
        representation['barber'] = BarberSerializer(instance.barber).data
        representation['service'] = ServiceSerializer(instance.service).data

        return representation

    def create(self, validated_data):
        customer = validated_data.pop("customer")
        customer, _ = CustomerModel.objects.get_or_create(
            email=customer.get("email"),
            document_number=customer.get("document_number"),
            defaults=customer,
        )

        appointment = AppointmentModel.objects.create(
            customer=customer,
            **validated_data
        )

        return appointment
