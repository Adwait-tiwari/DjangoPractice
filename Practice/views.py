from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from Practice.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from .serializer import StudentSerializer

# Home page
def home(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'Home.html')

# About page
def about(request):
    return render(request, 'About.html')

# Contact page
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, subject=subject, desc=desc)
        contact.save()
    return render(request, 'Contact.html')

# Login
def LoginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('login')
    return render(request, 'Login.html')

# Logout
def LogoutUser(request):
    logout(request)
    return render(request, 'login.html')

# Signup
def SignupUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm_password')

        if password != confirm:
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')
    return render(request, 'Signup.html')

# Simple API to check Django-React connection
def home_api(request):
    return JsonResponse({"message": "Hello from Django to React"})

@csrf_exempt
@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Student added successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)