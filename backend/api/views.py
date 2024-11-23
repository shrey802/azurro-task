from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Owner, Booking
from .serializers import OwnerSerializer, BookingSerializer

class OwnerCreateView(APIView):
    def post(self, request):
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingCreateView(APIView):
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



