from django.shortcuts import render, redirect
from .models import area

def home(request):

    return render(request, 'home.html')

def fingerling(request):
    areas = area.objects.all()
    return render(request, 'fingerling.html', {'areas': areas})

def areas(request):
    areas = area.objects.all()
    return render(request, 'areas.html', {'areas': areas})

def month(request):
    areas = area.objects.all()
    return render(request, 'month.html', {'areas': areas})

def tests(request):
    areas = area.objects.all()
    return render(request, 'test.html', {'areas': areas})
