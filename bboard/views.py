from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest

def index(request):
    return HttpResponse("Здесь будет выведен список объявлений.")
    
