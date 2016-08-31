from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner!")

def about(request):
    return HttpResponse("Rango says here is the <a href=\"/rango/\">about</a> page.")
