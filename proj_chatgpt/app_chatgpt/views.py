
from django.shortcuts import render

def home(request):
    if request.method == "POST":
        question = request.POST['question']
        return render(request,'home.html',{'question':question})
    return render(request,'home.html',{})
    

def about(request):
    return render(request,'about.html',{})

def dashboard(request):
    return render(request,'dashboard.html',{})

def prices(request):
    return render(request,'prices.html',{})
