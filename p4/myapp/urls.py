from django.urls import path 
from . import views 
urlpatterns = [
path('home/', views.home, name='home'), 
path('about_us/', views.about_us, name='about_us'), 
path('contact_us/', views.contact_us, name='contact_us'),
]