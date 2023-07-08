
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .serializers import UsersSerializer
from user.models import User
from django.shortcuts import render

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [

        {'POST': '/menus'},
        {'GET': '/menus'},
        {'GET': '/menus/:id'},
        {'PUT': '/menus/:id'},
        {'DELETE': '/menus/:id'},


        {'GET': '/api/user'},
        {'GET': '/users/login'},
        {'GET': '/users/logout'},
        {'GET': '/users/register'},
        {'GET': '/users'},
        {'GET': '/users/profile/:id'},
        {'GET': '/users/account'},
        {'GET': '/users/edit-account'},

        {'GET': '/admin'},

        {'GET': '/reset_password'},
        {'GET': '/reset_password_sent'},
        {'GET': '/reset/:id/:token'},
        {'GET': '/reset_password_complete'},

        {'POST': '/transactions'},
        {'GET': '/transactions'},
        {'GET': '/transactions/:id'},
        {'PUT': '/transactions/:id'},
        {'DELETE': '/transactions/:id'},


        {'POST': '/bookings'},
        {'GET': '/bookings'},
        {'GET': '/bookings/:id'},
        {'PUT': '/bookings/:id'},
        {'DELETE': '/bookings/:id'},



        {'POST': '/recipes'},
        {'GET': '/recipes'},
        {'GET': '/recipes/:id'},
        {'PUT': '/recipes/:id'},
        {'DELETE': '/recipes/:id'},


        {'POST': '/ingredients'},
        {'GET': '/ingredients'},
        {'GET': '/ingredients/:id'},
        {'PUT': '/ingredients/:id'},
        {'DELETE': '/ingredients/:id'},

        {'POST': '/orders'},
        {'GET': '/orders'},
        {'GET': '/orders/:id'},
        {'PUT': '/orders/:id'},
        {'DELETE': '/orders/:id'},

        {'POST': '/tabletop'},
        {'GET': '/tabletop'},
        {'GET': '/tabletop/:id'},
        {'PUT': '/tabletop/:id'},
        {'DELETE': '/tabletop/:id'},

        {'POST': '/item'},
        {'GET': '/item'},
        {'GET': '/item/:id'},
        {'PUT': '/item/:id'},
        {'DELETE': '/item/:id'},

        {'POST': '/itemChef'},
        {'GET': '/itemChef'},
        {'GET': '/itemChef/:id'},
        {'PUT': '/itemChef/:id'},
        {'DELETE': '/itemChef/:id'},

        {'POST': '/user/token'},
        {'POST': '/user/token/refresh'},
    ]
    return Response(routes)


@api_view(['GET'])
def getUsers(request):
    user = User.objects.all()
    serializer = UsersSerializer(user, many=True)
    return Response(serializer.data)
