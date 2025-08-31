from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=122,blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name if self.name else "Anonymous"
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name