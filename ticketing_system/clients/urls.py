from django.urls import path
from . views import  HomeView, DescriptionDetailView, PendingView
#from .views import description_detail

urlpatterns = [
    path('',HomeView.as_view(), name="home"),
    path('description_detail/',DescriptionDetailView.as_view(), name="description_detail"),
    path('pending/',PendingView.as_view(), name="pending"),
    #path('url/', description_detail, name='description_detail'),

]
