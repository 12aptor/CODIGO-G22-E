from rest_framework import serializers
from .models import CanchaModel, ReservaModel

class CanchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanchaModel
        fields = '__all__'
        # fields = ('id', 'nombre', 'direccion')
        # exclude = ('creado_en',)

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaModel
        fields = '__all__'