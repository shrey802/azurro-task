from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Owner, Booking
from .serializers import OwnerSerializer, BookingSerializer
from django.http import JsonResponse
from datetime import datetime

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

class BookingByTurfDateView(APIView):
    def get(self, request, *args, **kwargs):
        turf_id = request.query_params.get('turf_id')
        date_str = request.query_params.get('date')

        if not turf_id or not date_str:
            return JsonResponse({"detail": "Both 'turf_id' and 'date' are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()  # Convert string to date object
        except ValueError:
            return JsonResponse({"detail": "Invalid date format. Use 'YYYY-MM-DD'."}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch bookings for the given turf_id and date
        bookings = Booking.objects.filter(owner_turf_id__turf_id=turf_id, date=date_obj)

        if not bookings.exists():
            return JsonResponse({"detail": "No bookings found for the given turf and date."}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class OwnerLoginView(APIView):
    def get(self, request, *args, **kwargs):
        first_name = request.query_params.get('first_name')
        last_name = request.query_params.get('last_name')
        turf_name = request.query_params.get('turf_name')

        if not first_name or not last_name or not turf_name:
            return JsonResponse({"detail": "First name, last name, and turf name are required."}, status=400)

        # Check if the Owner exists with the provided information
        owners = Owner.objects.filter(
            first_name=first_name,
            last_name=last_name,
            turf_name=turf_name
        )

        if owners.exists():
            return Response([owner.turf_id for owner in owners])  # Return the turf_id for login
        else:
            return JsonResponse({"detail": "Owner not found or invalid credentials."}, status=404)
