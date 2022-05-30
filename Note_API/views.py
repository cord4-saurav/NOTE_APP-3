from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import NoteAPI
# from .serializers import Note_APISerializer
# from rest_framework.response import Response
# from rest_framework import viewsets
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from NoteProject import settings
from django.core.mail import send_mail


# Create your views here.
# from datetime import datetime
# class Note_APIViewSet(viewsets.ModelViewSet):
#     queryset = NoteAPI.objects.all()
#     serializer_class = Note_APISerializer


def home(request):
    return render(request, 'new/index.html')


def signup(request):
    if request.method == "post":
        username = request.post['username']
        Firstname = request.post['Firstname']
        Lastname = request.post['Lastname']
        Email = request.post['Email']
        Password = request.post['Password']
        ConfrimPassword = request.post['ConfrimPassword']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! please try another ")
            return redirect('home')

        if User.objects.filter(Email=Email):
            messages.error(request, "Email already registered")
            return redirect('home')

        if len(username)>10:
            messages.error(request, "username must be of 10 character")

        if Password != ConfrimPassword:
            messages.error(request, "password didn't match")

        user = User.objects.create_user(username, Email, Password, ConfrimPassword)
        user.first_name = Firstname
        user.last_name = Lastname

        user.save()

        messages.success(request, "your Account has been successfully created")

        # Welcome Email

        subject = "welcome To login page"
        message = "Hello" + user.first_name + "!! /n" + "welcome to login page! /n "
        form_email = settings.EMAIL_HOST_USER
        to_list = [user.email]
        send_mail(subject, message, form_email, to_list, fail_silently=True)

        return redirect('signin')

    return render(request, 'new/signup.html')


def signin(request):
    if request.method == 'post':
        username = request.post['username']
        password = request.post['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            username = user.frist_name
            messages.error(request, "successfully logged in")
            return render(request, "new/index.html", {"username": username})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')
    return render(request, 'new/signin.html')
#
#
def signout(request):
    logout(request)
    messages.success(request, "logged out successfully")
    return redirect('home')














