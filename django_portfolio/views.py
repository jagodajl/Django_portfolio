from django.http import HttpResponse
from django.shortcuts import render

def portfolio(request):
    #return HttpResponse('portfolio')
    return render(request, "portfolio.html")
