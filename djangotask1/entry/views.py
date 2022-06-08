from email import message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from entry.models import Signup
from .forms import SignupForm, LoginForm

# Create your views here.

def entry_page(request):
    return render(request, 'index.html')

def login_page(request):
    form = LoginForm()
    context = {'login_form':form}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            lusername = form.cleaned_data.get('username')
            lpassword = form.cleaned_data.get('password')
            bool_answer = Signup.objects.filter(username=lusername, password=lpassword).exists()
            if bool_answer:
                profile = Signup.objects.get(username = lusername, password = lpassword)
                username = profile.username
                email = profile.email
                address = profile.address
                fname = profile.fname
                lname = profile.lname
                role = profile.role
                context = {'role': role, 'fname':fname, 'lname':lname, 'email':email, 'address':address, 'username':username}
                return render(request, 'profile.html', context)
            else:
                message = 'Invalid credentials'
                context = {'message' : message, 'login_form':form}
                return render(request, 'login.html', context)
            

    return render(request, 'login.html', context)


def signup_page(request):
    form = SignupForm()
    password = ''
    confirm_password = ''
    message = ''
    context = {'singup_form':form}
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            if password != confirm_password:
                message = "Passwords not matching"
                context = {'signup_form': form, 'message' : message}
                return render(request, 'signup.html',context)
            form.save()
            form = SignupForm()
            message = "User created"
            context = {'signup_form': form, 'message' : message}
            return render(request, 'signup.html',context)
        else:
            message =  "Username already taken"
            context = {'signup_form': form, 'message' : message}
            return render(request, 'signup.html',context)

     
    form = SignupForm()
    context = {'signup_form': form, 'message' : message}
    return render(request, 'signup.html',context)