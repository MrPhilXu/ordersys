from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')


def register(request):
    return render(request,'register.html')    

def sign_up(request):
    return render(request,'sign_up.html')    