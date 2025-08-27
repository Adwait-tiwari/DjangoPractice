from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=122,blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name if self.name else "Anonymous"