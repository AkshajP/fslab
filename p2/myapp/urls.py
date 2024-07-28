from django.urls import path 
from . import views
urlpatterns = [
path('datetime_offsets/', views.datetime_offsets, name='datetime_offsets'),
]