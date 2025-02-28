from rest_framework import generics
from .models import CanchaModel
from .serializers import CanchaSerializer

class CanchaView(generics.ListCreateAPIView):
    queryset = CanchaModel.objects.all()
    serializer_class = CanchaSerializer

class AdministrarCanchaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CanchaModel.objects.all()
    serializer_class = CanchaSerializer