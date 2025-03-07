from rest_framework import generics, status
from rest_framework.response import Response
from django.http import Http404
from .models import (
    RoleModel,
)
from .serializers import (
    RoleSerializer,
    UserSerializer,
)

class RoleListView(generics.ListAPIView):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer

    def list(self, request):
        response = super().list(request)

        return Response({
            'object': 'list_roles',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class RoleCreateView(generics.CreateAPIView):
    serializer_class = RoleSerializer

    def create(self, request):
        response = super().create(request)

        return Response({
            'object': 'create_role',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class RoleUpdateView(generics.UpdateAPIView):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request)

            return Response({
                'object': 'update_role',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'object': 'update_role',
                'error': 'role not found'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class RoleDestroyView(generics.DestroyAPIView):
    queryset = RoleModel.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request)

            return Response({
                'object': 'destroy_role'
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'object': 'destroy_role',
                'error': 'role not found'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class RoleRetrieveView(generics.RetrieveAPIView):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super().retrieve(request)

            return Response({
                'object': 'retrieve_role',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'object': 'retrieve_role',
                'error': 'role not found'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class AuthRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request):
        pass