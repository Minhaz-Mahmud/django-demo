from django.shortcuts import render, redirect
# from models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required





def login_page(request):
    if request.method != "POST":
        return render(request, 'login.html')
    
   
    username = request.POST.get('username')
    password = request.POST.get('password')

    if  not User.objects.filter(username=username).exists():
        messages.error(request,'Invalid Username')
        return redirect ('/login/')

    user=authenticate(username=username,password=password)

    if user is None:
        messages.error(request,'Invalid Password')
        return redirect ('/login/')
    
    else:
        login(request,user)
        return redirect('/receipe/')

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method != "POST":
        return render(request, 'register.html')

    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user=User.objects.filter(username=username)

    if user.exists():
        messages.info(request, "Username Already Exists")
        return redirect('/register/')
    

    user = User.objects.create(
        first_name=first_name,
        last_name=last_name,
        username=username
    )
    user.set_password(password)
    user.save()
      
    messages.info(request, "Account Created Successfully")
    return redirect('/register/')



@login_required(login_url='/login/')
def receipe(request):
    return render(request, 'receipe.html')
