
from django.urls import path
from .views import register, EnterpriseLoginView, EnterpriseLogoutView, dashboard

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', EnterpriseLoginView.as_view(), name='login'),
    path('logout/', EnterpriseLogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]
