from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TransactionList.as_view(), name="transactions"),
    path('<int:pk>/', views.TransactionDetail.as_view(), name="transactionitem"),
]

