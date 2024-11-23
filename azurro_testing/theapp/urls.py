
from django.urls import path

from .api_views import RegisterAPIView,LoginAPIView,LogoutAPIView,DashboardAPIView
from .views import register, EnterpriseLoginView, EnterpriseLogoutView, dashboard

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', EnterpriseLoginView.as_view(), name='login'),
    path('logout/', EnterpriseLogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
path('api/register/', RegisterAPIView.as_view(), name='api-register'),
    path('api/login/', LoginAPIView.as_view(), name='api-login'),
    path('api/logout/', LogoutAPIView.as_view(), name='api-logout'),
    path('api/dashboard/', DashboardAPIView.as_view(), name='api-dashboard'),
]
