from django.shortcuts import render,get_object_or_404, redirect

# Create your views here.
from .models import Mamber

def home(request):
    template_name = 'index.html'
    context = {'title':"Class of 20"}
    return render(request,template_name,context)

def mambers(request):
    template_name = 'mambers.html'
    infor = Mamber.objects.all()
    context = {'title': 'Mambers','infor':infor}
    return render(request,template_name,context)

def mamber(request, slug):
    template_name = 'mamber.html'
    infor = get_object_or_404(Mamber, slug=slug)
    context = {'title':infor.name,'infor':infor}
    return render(request,template_name,context)
