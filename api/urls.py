from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('user/', views.getUsers, name="user"),
]
