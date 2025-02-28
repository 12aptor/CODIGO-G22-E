from rest_framework import serializers
from .models import CanchaModel

class CanchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanchaModel
        fields = '__all__'
        # fields = ('id', 'nombre', 'direccion')
        # exclude = ('creado_en',)