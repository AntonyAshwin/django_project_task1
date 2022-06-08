from django.db import models
from django.forms import PasswordInput, Form, CharField

class Signup(models.Model):  
    ROLE = (
    ('DOCTOR','DOCTOR'),
    ('PATIENT', 'PATIENT'),
    )

    fname = models.CharField(max_length=32)  
    lname = models.CharField(max_length=32)  
    profile_picture = models.ImageField(null = True, blank = True, upload_to = "images/")
    role = models.CharField(max_length = 32, choices=ROLE, default='PATIENT')
    username = models.CharField(max_length=32, primary_key=True)  
    email = models.EmailField()
    password = models.CharField(max_length = 50)
    confirm_password = models.CharField(max_length = 50)
    address = models.CharField(max_length=100)  

    def __str__(self):
        return self.username
    
    class Meta:  
        db_table = "signupform"  

class Login(models.Model):  
    username = models.CharField(max_length=42)
    password = models.CharField(max_length=100)

    class Meta:  
        db_table = "loginform"  