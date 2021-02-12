from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User


class AccountRegistrationForm(UserCreationForm):

    YEARS = [x for x in range(1900, 2020)]
    email = forms.EmailField(max_length=60, help_text='Required field. Add a valid email address.')
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))

    class Meta:
        model = User
        field = ['email', 'username', 'password1', 'password2', 'first_name', 'last_name',
                 'phone_number', 'address', 'city']
        exclude = ['is_active', 'is_admin', 'is_staff', 'is_superuser', 'last_login', 'date_joined', 'password']

