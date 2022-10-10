from django.shortcuts import render
def infos_list(request):
    return render(request, "infos/infos_list.html")

def me(request):
    #return HttpResponse("me")
    return render(request, "infos/me.html")

def contact(request):
    #return HttpResponse("contact")
    return render(request, "infos/contact.html")
