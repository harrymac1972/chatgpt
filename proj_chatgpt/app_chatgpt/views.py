
import os
from django.shortcuts import render
import openai
from dotenv import load_dotenv

load_dotenv()

def home(request):
    if request.method == "POST":
        question = request.POST['question']
        
        api_key = os.environ.get('OPEN_AI_KEY')
        openai.api_key = api_key

        response = get_api_response(question) # <-- problem

        return render(request,'home.html',{'question':question,
                                            'api_key':api_key})
    return render(request,'home.html',{})
    

def about(request):
    return render(request,'about.html',{})

def dashboard(request):
    return render(request,'dashboard.html',{})

def prices(request):
    return render(request,'prices.html',{})




def get_api_response(question):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response

