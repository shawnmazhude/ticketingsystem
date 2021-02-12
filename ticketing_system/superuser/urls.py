from django.urls import path
from . views import  ClientInfoView, PendingView, UserHomeView


urlpatterns = [
    
    path('ticket_mgt',UserHomeView.as_view(), name="ticket_mgt"),
    path('client_info/',ClientInfoView.as_view(), name="client_info"),
    path('client_enq/',PendingView.as_view(), name="client_enq"),
]