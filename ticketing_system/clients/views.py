from django.shortcuts import render, redirect
from . models import Client, NewFaultReport
from . forms import PostForm, DescripDetForm
from django.views.generic import CreateView, ListView
#from accounts.models import user_type


class HomeView(ListView):
    model = NewFaultReport
    template_name = 'tickets_inprogress.html'


class DescriptionDetailView(CreateView):
    model = NewFaultReport
    form_class = DescripDetForm
    template_name = 'description_details.html'
    #fields = '__all__'


class PendingView(ListView):
    model = NewFaultReport
    template_name = 'pending.html'
    



