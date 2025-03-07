from django.urls import path
from .views import *

urlpatterns = [
    path('roles/list', RoleListView.as_view()),
    path('roles/create', RoleCreateView.as_view()),
    path('roles/update/<int:pk>', RoleUpdateView.as_view()),
    path('roles/destroy/<int:pk>', RoleDestroyView.as_view()),
    path('roles/retrieve/<int:pk>', RoleRetrieveView.as_view()),

    path('auth/register', AuthRegisterView.as_view()),
]