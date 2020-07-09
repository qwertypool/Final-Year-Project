from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 150)
    email = models.EmailField()
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    

    