from django.forms import ModelForm
from .models import Signup, Login
from django import forms

class SignupForm(ModelForm):
    class Meta:
        model = Signup
        fields = "__all__"

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = "__all__"

        widgets = {
            # telling Django your password field in the mode is a password input on the template
            'password': forms.PasswordInput() 
        }