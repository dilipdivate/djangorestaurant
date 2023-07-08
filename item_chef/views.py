from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from item_chef.models import ItemChef
from .serializers import ItemChefSerializer
from rest_framework import generics

# Create your views here.

class ItemChefList(generics.ListCreateAPIView):
    queryset = ItemChef.objects.all()
    serializer_class = ItemChefSerializer


class ItemChefDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemChef.objects.all()
    serializer_class = ItemChefSerializer