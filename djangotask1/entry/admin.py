from django.contrib import admin
from .models import Signup

# Register your models here.
class Users (admin.ModelAdmin):
    list_display=('fname','lname','profile_picture','role','username','email','password', 'confirm_password','address')

admin.site.register(Signup,Users)