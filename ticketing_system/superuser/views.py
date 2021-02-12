from django.shortcuts import render
from accounts.models import User, user_type
from . models import Client_Info
from clients.models import NewFaultReport
from django.views.generic import ListView

# Create your views here.
class UserHomeView(ListView):
    model = Client_Info
    template_name= 't_management.html'

class ClientInfoView(ListView):
    model = User
    template_name = 'client_info.html'
 

class PendingView(ListView):
    model = NewFaultReport
    template_name = 'client_enq.html'