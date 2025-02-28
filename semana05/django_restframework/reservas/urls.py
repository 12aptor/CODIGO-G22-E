from django.urls import path
from .views import (
    CanchaView,
    AdministrarCanchaView,
)

urlpatterns = [
    path('canchas', CanchaView.as_view()),
    path('canchas/<int:pk>', AdministrarCanchaView.as_view()),
]