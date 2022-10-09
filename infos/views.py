from django.shortcuts import render

# Create your views here.

def infos(request):
    #return HttpResponse("me")
    return render(request, 'templates/infos/infos.html')

def me(request):
    #return HttpResponse("me")
    return render(request, "templates/infos/me.html")

def contact(request):
    #return HttpResponse("contact")
    return render(request, "templates/infos/contact.html")
