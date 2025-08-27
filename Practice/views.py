from django.shortcuts import render
from django.http import HttpResponse
from Practice.models import Contact

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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,subject=subject,desc=desc)
        contact.save()
    return render(request,'Contact.html')

    # return HttpResponse("this is the  contact page")