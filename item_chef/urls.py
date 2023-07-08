from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.ItemChefList.as_view(), name="itemChef"),
    path('<int:pk>/', views.ItemChefDetail.as_view(), name="itemChefdetail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)