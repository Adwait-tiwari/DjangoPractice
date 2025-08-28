from django.shortcuts import render,redirect
from django.http import HttpResponse
from Practice.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'Home.html')
    # return HttpResponse("This is the first Django Project")

def about(request):
    return render(request,'About.html')
    # return HttpResponse("This is the about page")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,subject=subject,desc=desc)
        contact.save()
    return render(request,'Contact.html')

    # return HttpResponse("this is the  contact page")

def LoginUser(request):
    if request.method == 'POST':
         username = request.POST.get('username')
         password =request.POST.get('password')

         user = authenticate(request,username=username,password=password)

         if user is not None:
             login(request,user)
             return redirect('/')
         else:
             return redirect('login')
         
    return render(request,'Login.html')

def LogoutUser(request):
    logout(request)
    return render(request,'Logout.html')
