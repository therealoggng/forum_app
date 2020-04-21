#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("я тот который всех тащиит")
# Create your views here.
