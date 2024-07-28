from django.urls import path 
from . import views 
urlpatterns = [
path('student_list/', views.StudentListView.as_view(), name='student_list'), 
path('student_detail/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
]