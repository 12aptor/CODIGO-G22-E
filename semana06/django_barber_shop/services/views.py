from rest_framework import generics, status
from rest_framework.response import Response
from django.http import Http404
from .models import (
    ServiceModel,
    BarberModel,
)
from .serializers import (
    ServiceSerializer,
    BarberSerializer,
)

class ServiceListView(generics.ListAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        return Response({
            'object': 'list_services',
            'data': response.data
        }, status=status.HTTP_200_OK)

class ServiceCreateView(generics.CreateAPIView):
    serializer_class = ServiceSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        return Response({
            'object': 'create_service',
            'data': response.data
        }, status=status.HTTP_200_OK)

class ServiceUpdateView(generics.UpdateAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)

            return Response({
                'object': 'update_service',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'object': 'update_service',
                'error': 'service not found'
            }, status=status.HTTP_400_BAD_REQUEST)

class ServiceDestroyView(generics.DestroyAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)

            return Response({
                'object': 'destroy_service',
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'object': 'destroy_service',
                'error': 'service not found'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class ServiceRetrieveView(generics.RetrieveAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super().retrieve(request, *args, **kwargs)

            return Response({
                'object': 'retrieve_service',
                'data': response.data
            })
        except Http404:
            return Response({
                'object': 'retrieve_service',
                'error': 'service not found'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class BarberListView(generics.ListAPIView):
    queryset = BarberModel.objects.all()
    serializer_class = BarberSerializer

    def get_queryset(self):
        return BarberModel.objects.filter(status=True)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        return Response({
            'object': 'list_barbers',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class BarberCreateView(generics.CreateAPIView):
    serializer_class = BarberSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        return Response({
            'object': 'create_barber',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class BarberUpdateView(generics.UpdateAPIView):
    queryset = BarberModel.objects.all()
    serializer_class = BarberSerializer

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)

            return Response({
                'object': 'update_barber',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'object': 'update_barber',
                'error': 'barber not found'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class BarberDestroyView(generics.DestroyAPIView):
    queryset = BarberModel.objects.all()
    # serializer_class = BarberSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.status = False
            instance.save()

            # serializer = self.get_serializer(instance)

            return Response({
                'object': 'destroy_barber'
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'object': 'destroy_barber',
                'error': 'barber not found'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class BarberRetrieveView(generics.RetrieveAPIView):
    queryset = BarberModel.objects.all()
    serializer_class = BarberSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super().retrieve(request, *args, **kwargs)

            return Response({
                'object': 'retrieve_barber',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'object': 'retrieve_barber',
                'error': 'barber not found'
            }, status=status.HTTP_400_BAD_REQUEST)