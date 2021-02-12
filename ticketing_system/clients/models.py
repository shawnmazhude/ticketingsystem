from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from accounts.models import User

# Create your models here.
class Client(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.username) 


class NewFaultReport(models.Model):
    Enq_No = models.AutoField( primary_key=True,verbose_name='Enq #')
    Subject_Title = models.TextField(verbose_name="Subject Title", blank=True)
    description = models.TextField(verbose_name="Full Problem or Request Description", blank=True)
    date_created = models.DateField(verbose_name="Date Resolution Expected (mandatory)", blank=True)
    time = models.TimeField(null=True, blank=True)

    
    def __str__(self):
        return self.Subject_Title 

    def get_absolute_url(self):
        return reverse('home')
