from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.IngredientList.as_view(), name="ingredients"),
    path('<int:pk>/', views.IngredientDetail.as_view(), name="ingredientitem"),
]

urlpatterns = format_suffix_patterns(urlpatterns)