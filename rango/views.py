from django.shortcuts import render
from django.http import HttpResponse

# import the category model
from rango.models import Category

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list} 
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says here is the <a href=\"/rango/\">about</a> page.")
