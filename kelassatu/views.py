from django.shortcuts import render

# Create your views here.
def isikelassatu(request):
    return render (request, 'kelassatu.html')