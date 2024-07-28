from django.http import HttpResponse 
from django.shortcuts import render 
from django.views import generic
from .models import Course, Student
class StudentListView(generic.ListView): 
    model = Student
    template_name = "student_list.html"
class StudentDetailView(generic.DetailView): 
    model = Student
    template_name = "student_detail.html"