from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Turf
from .serializers import EnterpriseUserSerializer, TurfSerializer


# Registration API View (Generic View)
class RegisterAPIView(CreateAPIView):
    serializer_class = EnterpriseUserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.get_or_create(user=user)


# Login API View (Custom APIView)
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "message": "Login successful.",
                "token": token.key
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


# Logout API View (Custom APIView)
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)


# Dashboard API View (Generic View)
class DashboardAPIView(ListAPIView):
    serializer_class = TurfSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return turfs owned by the authenticated user
        return Turf.objects.filter(owner=self.request.user)
