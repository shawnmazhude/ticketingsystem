from django.db import models
from accounts.models import User

# Create your models here.
class Client_Info(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)