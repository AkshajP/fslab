from django.urls import path 
from . import views 
urlpatterns = [
path('add_project/', views.add_project), 
path('projectreg/',views.add_project1)
]