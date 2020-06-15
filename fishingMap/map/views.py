from django.shortcuts import render, redirect
from .models import area, fingerling, branches, fishingStatus
from .forms import fishingStatusForm

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

def fishingStatusReport(request):
    if request.method == "POST":
        form = fishingStatusForm(request.POST, request.FILES)
        if form.is_valid():
            status = form.save(commit=False)
            status.save()
            return redirect('/')
    else:
        form = fishingStatusForm()
    return render(request, 'fishingStatusReport.html', {'form': form})
