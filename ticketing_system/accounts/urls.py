from django.urls import path, include
from.views import register_user
#from .views import UserRegisterView

urlpatterns = [
    #path('register/', UserRegisterView.as_view(), name='register'),
    path('register/', register_user, name='register'),
    
]
