from django.urls import path
from .views import (
    CanchaView,
    AdministrarCanchaView,
    ReservaView,
)

urlpatterns = [
    path('canchas', CanchaView.as_view()),
    path('canchas/<int:pk>', AdministrarCanchaView.as_view()),
    path('reservas', ReservaView.as_view()),
]