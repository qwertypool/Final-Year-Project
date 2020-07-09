from django.db import models

# Create your models here.
class Lost(models.Model):
    #CARDS_CHOICES=[('adhar','Adhar Card'),('voterid','Voter Id Card'),('passport','Passport'),('atm','Atm Card')]
    name = models.CharField(max_length = 150)
    email = models.EmailField()
    uid = models.IntegerField()
    #card = models.CharField(max_length = 50,choices=CARDS_CHOICES,default='Adhar Card')
    card = models.CharField(max_length = 50,default='Adhar Card')
    details = models.TextField(blank=True)
    

class Found(models.Model):
    #CARDS_CHOICES=[('adhar','Adhar Card'),('voterid','Voter Id Card'),('passport','Passport'),('atm','Atm Card')]
    name = models.CharField(max_length = 150)
    email = models.EmailField()
    cardholder_name = models.CharField(max_length = 150)
    uid = models.IntegerField()
    #card = models.CharField(max_length = 50,choices=CARDS_CHOICES,default='Adhar Card')
    card = models.CharField(max_length = 50,default='Adhar Card')
    details = models.TextField(blank=True)