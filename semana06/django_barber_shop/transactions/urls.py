from django.urls import path
from .views import *

urlpatterns = [
    path("appointments/create", AppointmentCreateView.as_view()),

    path("payments/create/<int:appointment_id>", PaymentCreateView.as_view()),
]
