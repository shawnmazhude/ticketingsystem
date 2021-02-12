from django.contrib import admin
from . models import Client, NewFaultReport

# Register your models here.
admin.site.register(Client)
admin.site.register(NewFaultReport)
