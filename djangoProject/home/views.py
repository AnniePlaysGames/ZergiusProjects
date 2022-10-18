from django.shortcuts import render
from django.http import HttpResponse

from . import models

def home(request):
    return HttpResponse("this is home page")

def mybesthome(request):
    return render(request, 'index.html')

def get_all_persons(request):
    models.Person.objects.create(name='Sergey', age=21)
    persons = models.Person.objects.all()
    return render(request, 'home/index.html', {'persons': persons})
