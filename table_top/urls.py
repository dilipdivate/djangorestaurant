from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TableTopList.as_view(), name="tabletop"),
    path('<int:pk>/', views.TableTopDetail.as_view(), name="tabletopitem"),
]

