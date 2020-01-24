from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login

# Create your views here.


def get_login_page(req):
    return render(req,"login.html")

def post_login(req):
    username=req.POST["username"]
    password=req.POST["password"]
    user=authenticate(username=username,password=password)
    if user is not None:
        login(req,user)
        
        return redirect('home')
    else:
        return redirect('login')


def get_sign_up(req):
    return render(req,"signup.html")

def post_sign_up(req):
    username=req.POST["username"]
    password=req.POST["password"]
    email=req.POST["email"]
    print(username,email)
    user=User.objects.create_user(username=username,password=password,email=email)
    user.save()
    return redirect("home")

def user_logout(req):
    logout(req)
    return redirect('login')