from django.urls import path
from .views import *

urlpatterns = [
    path('services/list', ServiceListView.as_view()),
    path('services/create', ServiceCreateView.as_view()),
    path('services/update/<int:pk>', ServiceUpdateView.as_view()),
    path('services/destroy/<int:pk>', ServiceDestroyView.as_view()),
    path('services/retrieve/<int:pk>', ServiceRetrieveView.as_view()),

    path('barbers/list', BarberListView.as_view()),
    path('barbers/create', BarberCreateView.as_view()),
    path('barbers/update/<int:pk>' , BarberUpdateView.as_view()),
    path('barbers/destroy/<int:pk>', BarberDestroyView.as_view()),
    path('barbers/retrieve/<int:pk>', BarberRetrieveView.as_view()),
    path('barbers/available/<str:day>/<str:hour>', BarberAvailableView.as_view()),

    path('schedules/list', ScheduleListView.as_view()),
    path('schedules/create', ScheduleCreateView.as_view()),
]