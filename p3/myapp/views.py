from django.shortcuts import render 
from datetime import date
from django.http import HttpResponse
from django.template import Context, Template
def showlist(request):
    fruits = ["Grapes", "Orange", "Banana", "Jackfruit"] 
    students = ["Nemo", "Riya","Yoomfi","Nini"]
    return render(request, 'showlist.html', {"fruits":fruits, "students": students})