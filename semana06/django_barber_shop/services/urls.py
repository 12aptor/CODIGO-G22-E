from django.urls import path
from .views import *

urlpatterns = [
    path('services/list', ServiceListView.as_view()),
    path('services/create', ServiceCreateView.as_view()),
    path('services/update/<int:pk>', ServiceUpdateView.as_view()),
    path('services/destroy/<int:pk>', ServiceDestroyView.as_view()),
    path('services/retrieve/<int:pk>', ServiceRetrieveView.as_view()),
]