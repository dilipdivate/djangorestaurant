from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from menu.models import Menu
from rest_framework import status,serializers
from .serializers import MenusSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def getMenus(request):
    """
    List all Menus, or create a new Menu.
    """
    if request.method == 'GET':
        # checking for the parameters from the URL
        if request.query_params:
            items = Menu.objects.filter(**request.query_params.dict())
        else:
            menus = Menu.objects.all()

        # if there is something in items else raise error
        if menus:
            serializer = MenusSerializer(menus, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


    elif request.method == 'POST':
        # def perform_create(self, serializer):
        #     serializer.save(owner=self.request.user)
        serializer = MenusSerializer(data=request.data)
        if Menu.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This data already exists')

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def MenuItemDetail(request,pk):
    """
    Retrieve, update or delete a Menu.
    """
    try:
        menus = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MenusSerializer(menus, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MenusSerializer(menus, data=request.data,many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        menus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def postMenu(request, pk):
#     menu = Menu.objects.get(id=pk)
#     user = request.user.profile
#     data = request.data

#     serializer = MenusSerializer(menu, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# # @permission_classes([IsAuthenticated])
# def postMenu(request):
#     menu = Menu.objects.get()
#     # user = request.user.profile
#     data = request.data

#     serializer = MenusSerializer(menu, many=False)
#     return Response(serializer.data)

