
from django.shortcuts import render

def home(request):
    return render(request,'home.html',{})

def about(request):
    return render(request,'about.html',{})

def dashboard(request):
    return render(request,'dashboard.html',{})

def prices(request):
    return render(request,'prices.html',{})
