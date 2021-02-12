from django.shortcuts import render, redirect
from . models import User, user_type
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import AccountRegistrationForm
#from django.views import generic
from django.urls import reverse_lazy

# Create your views here.

def register_user(request):
    template_name = 'registration/register.html'
    context = {}
    if request.POST:
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['form'] = form
    else:
        form = AccountRegistrationForm
        context['form'] = form
    return render(request, template_name, context)



#def login(request):
 #   if (request.method == 'POST'):
  ##     password = request.POST.get('password') #Get password value from form
    #    user = authenticate(request, email=email, password=password)
       
     #   if user is not None:
      #      login(request, user)
       #     type_obj = user_type.objects.get(user=user)
        #    if user.is_authenticated and type_obj.is_client:
         #       return redirect('shome') #Go to student home
   #         elif user.is_authenticated and type_obj.is_spuser:
    ##            return redirect('thome') #Go to teacher home
      #  else:
        # Invalid email or password. Handle as you wish
        #    return redirect('login')
       # return render(request, 'login.html')