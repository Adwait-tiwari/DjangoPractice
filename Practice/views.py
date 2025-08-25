from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        "variable" : "This is the Home page of everything"
    }
    return render(request,'Home.html',context)
    # return HttpResponse("This is the first Django Project")

def about(request):
    return render(request,'About.html')
    # return HttpResponse("This is the about page")

def contact(request):
    return render(request,'Contact.html')

    # return HttpResponse("this is the  contact page")