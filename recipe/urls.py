from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.RecipeList.as_view(), name="recipes"),
    path('<int:pk>/', views.RecipeDetail.as_view(), name="recipeitem"),
]

