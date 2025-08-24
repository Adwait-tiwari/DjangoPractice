from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def request(request):
    return HttpResponse("This is the first Django Project")