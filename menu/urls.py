from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getMenus, name="menus"),
    path('<int:pk>/', views.MenuItemDetail, name="menuitem"),

]
