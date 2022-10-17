from django.shortcuts import render

# Create your views here.
def isikelastiga(request):
    return render (request, 'kelastiga.html')
