from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    AppointmentSerializer,
)

class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer

    def create(self, request):
        response = super().create(request)

        return Response({
            'object': 'create_appointment',
            'data': response.data
        }, status=status.HTTP_200_OK)

class PaymentCreateView(APIView):
    def post(self, request):
        pass