from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from booking.models import Booking
from .serializers import BookingSerializer
from rest_framework import status

# Create your views here.

# @api_view(['GET'])
# def getBookings(request):
#     bookings = Booking.objects.all()
#     serializer = BookingSerializer(bookings, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getBookingItem(request,pk):
#     bookings = Booking.objects.get(id=pk)
#     serializer = BookingSerializer(bookings, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def postBooking(request, pk):
#     booking = Booking.objects.get(id=pk)
#     user = request.user.profile
#     data = request.data

#     serializer = BookingSerializer(booking, many=False)
#     return Response(serializer.data)


# @api_view(['DELETE'])
# def removeBooking(request,pk):

#     booking = Booking.objects.get(id=pk)

#     booking.remove(id)
#     return Response('Booking was deleted!')

class BookingList(APIView):
    """
    List all snippets, or create a new booking.
    """

    def get(self, request, format=None):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            valid_data = serializer.data
            firstName = valid_data.get("firstName")
            lastName = valid_data.get("lastName")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingDetail(APIView):
    """
    Retrieve, update or delete a booking instance.
    """
    def get_object(self, pk):
        try:
            return Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        booking = self.get_object(pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        booking = self.get_object(pk)
        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        booking = self.get_object(pk)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)