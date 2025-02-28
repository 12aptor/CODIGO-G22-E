from rest_framework import generics, status
# from rest_framework.generics import (
#     ListAPIView, # Lista todos los registros
#     CreateAPIView, # Crear un registro
#     UpdateAPIView, # Actualizar un registro
#     DestroyAPIView, # Eliminar un registro
#     RetrieveAPIView, # Recuperar un registro
#     ListCreateAPIView, # Lista todos los registros y crear un registro
#     RetrieveUpdateDestroyAPIView, # Recuperar, actualizar y eliminar un registro
#     RetrieveDestroyAPIView, # Recuperar y eliminar un registro
#     GenericAPIView, # Un vista genérica
# )
from .models import CanchaModel, ReservaModel
from .serializers import CanchaSerializer, ReservaSerializer
from rest_framework.response import Response

class CanchaView(generics.ListCreateAPIView):
    queryset = CanchaModel.objects.all()
    serializer_class = CanchaSerializer

class AdministrarCanchaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CanchaModel.objects.all()
    serializer_class = CanchaSerializer

class ReservaView(generics.ListCreateAPIView):
    # queryset = ReservaModel.objects.all()
    serializer_class = ReservaSerializer

    def get_queryset(self):
        # return ReservaModel.objects.order_by('-id')
        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        print(request.headers)
        response = super().list(request, *args, **kwargs)
        return Response({
            'message': 'Lista de reservas',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        print(request.data)
        response = super().create(request, *args, **kwargs)
        return Response({
            'message': 'Reserva creada',
            'data': response.data
        }, status=status.HTTP_201_CREATED)
