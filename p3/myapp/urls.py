from django.urls import path 
from . import views
urlpatterns = [
path('showlist/', views.showlist, name='showlist'),
]