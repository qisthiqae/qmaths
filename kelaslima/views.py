from django.shortcuts import render

# Create your views here.
def isikelaslima(request):
    return render (request, 'kelaslima.html')