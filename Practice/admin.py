from django.contrib import admin
from Practice.models import Contact
from .models import Student


# Register your models here.
admin.site.register(Contact)
admin.site.register(Student)