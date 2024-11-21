
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import EnterpriseUserRegistrationForm


# Registration View
def register(request):
    if request.method == 'POST':
        form = EnterpriseUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            return redirect('dashboard')  # Redirect to the dashboard after registration
    else:
        form = EnterpriseUserRegistrationForm()
    return render(request, 'theapp/register.html', {'form': form})


# Login View
class EnterpriseLoginView(LoginView):
    template_name = 'theapp/login.html'


# Logout View
class EnterpriseLogoutView(LogoutView):
    next_page = 'login'  # Redirect to login page after logout


# Protected Dashboard View
@login_required
def dashboard(request):
    return render(request, 'theapp/dashboard.html')
