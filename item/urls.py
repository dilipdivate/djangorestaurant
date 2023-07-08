from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.ItemList.as_view(), name="items"),
    path('<int:pk>/', views.ItemDetail.as_view(), name="itemdetail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)