
from .models import Post
from datetime import datetime
from email import message
from urllib import request
from cv2 import WINDOW_AUTOSIZE, namedWindow
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from pathlib import Path
import os
from django.contrib.auth.decorators import login_required
import datetime
from datetime import timedelta


# Create your views here.

def login(request):
    if request.method == "POST":
        username= request.POST['username'] 
        password = request.POST['pass']

        if username=='admin':   
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("auth/")
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('/')
        else:
            try:
                user=auth.authenticate(username=User.objects.get(email=username), password=password)
            except:
                user=auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect("home/")
                else:
                    messages.error(request, 'Invalid credentials')
                    return redirect('/')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        conf_pass = request.POST['confirm_pass']
        email = request.POST['email']
        print(email)           
                  
        if password==conf_pass:
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email is already registered!')            
                return redirect('/register')

            elif User.objects.filter(username=username).exists():
                messages.error(request,'Username already taken!')
                return redirect('/register')
                  
            else: 
                user = User.objects.create_user(email=email, username=username, password=conf_pass)
                user.save()
                print("saved")
                return redirect('/')

        else:
            messages.error(request,'Password and confirm password does not match!')
            return redirect('/register')

    else:
        return render(request,'register.html')

@login_required(login_url="/")
def index(request):
    features = Post.objects.all()
    return render(request, 'index.html', {'features' : features})

@login_required(login_url="/")
def home(request):
    if request.method == 'POST':
        img = request.POST['imgs']
        addr = request.POST['address']
        time = datetime.datetime.now()
        new_Post = Post(image=img, address = addr, dated = time)
        Post.save()

    return render(request, 'home.html')


@login_required(login_url="/")
def notifications(request):
    return render(request, 'notification.html')

@login_required(login_url="/")
def doubts(request):
    return render(request, 'doubts.html')

@login_required(login_url="/")
def recents(request):
    return render(request, 'recents.html')

@login_required(login_url="/")
def admin(request):
    return render(request, 'admin.html')

@login_required(login_url="/")
def admindoubts(request):
    return render(request, 'admindoubts.html')


def logout(request):
        auth.logout(request)
        return redirect("/")
