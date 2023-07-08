from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from table_top.models import TableTop
from .serializers import TableTopSerializer
from rest_framework import generics

# Create your views here.


class TableTopList(generics.ListCreateAPIView):
    queryset = TableTop.objects.all()
    serializer_class = TableTopSerializer


class TableTopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TableTop.objects.all()
    serializer_class = TableTopSerializer