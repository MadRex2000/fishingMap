from django.shortcuts import render, redirect
from .models import area, fingerling, branches

def home(request):
    areas = area.objects.all()
    return render(request, 'home.html', {'areas': areas})

def fish(request):
    areas = area.objects.all()
    fishes = fingerling.objects.all()
    branch = branches.objects.all()
    return render(request, 'fingerling.html', {'areas': areas, 'fingerling': fishes, 'branches': branch,})

def areas(request):
    areas = area.objects.all()
    return render(request, 'areas.html', {'areas': areas})

def tests(request):
    areas = area.objects.all()
    fishes = fingerling.objects.all()
    branch = branches.objects.all()
    return render(request, 'test.html', {'areas': areas, 'fingerling': fishes, 'branches': branch,})
