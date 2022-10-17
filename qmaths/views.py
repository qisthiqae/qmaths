from django.shortcuts import render
from django.template import loader

def isiqmaths(request):
    return render (request, 'index.html')