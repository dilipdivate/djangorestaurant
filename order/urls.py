from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.OrderList.as_view(), name="orders"),
    path('<int:pk>/', views.OrderDetail.as_view(), name="orderitem"),
]

