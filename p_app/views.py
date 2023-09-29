from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signIn(request):
    return render(request, 'signIn.html')

def signup(request):
    return render(request, 'signup.html')