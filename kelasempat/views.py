from django.shortcuts import render

# Create your views here.
def isikelasempat(request):
    return render (request, 'kelasempat.html')