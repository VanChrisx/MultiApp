from django import forms
from django.contrib.auth.forms import UserCreationForm
from season.models import User
# Create your models here.


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
