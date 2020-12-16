from django.urls import path
from.import views

urlpatterns = [
    
    path('', views.home,name='home'),
    path('about/', views.aboutus,name='about'),
    
    path('service/', views.service,name='service'),
    path('privacypolice/', views.privacypolice,name='privacypolice'),
    
    path('termsinservice/', views.termsinservice,name='termsinservice'),
    
   
   
    
    
    
   
]
