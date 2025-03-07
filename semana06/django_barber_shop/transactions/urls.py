from django.urls import path
from .views import *

urlpatterns = [
    path("appointments/create", AppointmentCreateView.as_view()),
]
