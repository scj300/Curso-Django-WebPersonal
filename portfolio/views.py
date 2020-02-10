from django.shortcuts import render, HttpResponse

# Create your views here.

def portfolio(request):
    return render(request, "portfolio/home.html")
