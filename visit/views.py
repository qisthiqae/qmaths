from django.shortcuts import render

# Create your views here.
def isivisit(request):
    return render (request, 'visit.html')