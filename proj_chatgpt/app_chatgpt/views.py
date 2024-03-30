
from django.shortcuts import render
import openai


def home(request):
    if request.method == "POST":
        question = request.POST['question']
        api_key = get_api_key()
        openai.api_key = api_key
        return render(request,'home.html',{'question':question,
                                            'api_key':api_key})
    return render(request,'home.html',{})
    

def about(request):
    return render(request,'about.html',{})

def dashboard(request):
    return render(request,'dashboard.html',{})

def prices(request):
    return render(request,'prices.html',{})

# workaround to get environment variable for now
def get_api_key():    
    key_h = r"\Users\harry\open_ai_key.txt"
    with open(key_h, 'r') as file:
        key_v = file.read()
    return key_v

