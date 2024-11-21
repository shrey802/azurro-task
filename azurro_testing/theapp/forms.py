from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import EnterpriseUser

class EnterpriseUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = EnterpriseUser
        fields = ['username', 'email', 'company_name', 'password1', 'password2']
