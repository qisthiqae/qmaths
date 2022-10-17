from django.shortcuts import render

# Create your views here.
def isikamus(request):
    return render (request, 'kamus.html')