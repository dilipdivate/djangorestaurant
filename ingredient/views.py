from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from ingredient.models import Ingredient
from .serializers import IngredientSerializer
from rest_framework import generics

# Create your views here.

# @api_view(['GET'])
# def getIngredients(request):
#     ingredients = Ingredient.objects.all()
#     serializer = IngredientSerializer(ingredients, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def postIngredient(request, pk):
#     ingredient = Ingredient.objects.get(id=pk)
#     user = request.user.profile
#     data = request.data

#     serializer = IngredientSerializer(ingredient, many=False)
#     return Response(serializer.data)


# @api_view(['DELETE'])
# def removeIngredient(request,pk):

#     ingredient = Ingredient.objects.get(id=pk)

#     ingredient.remove(id)
#     return Response('Ingredient was deleted!')


class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer