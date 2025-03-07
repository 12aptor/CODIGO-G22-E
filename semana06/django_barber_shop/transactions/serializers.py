from rest_framework import serializers
from .models import (
    AppointmentModel,
)


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentModel
        fields = "__all__"
