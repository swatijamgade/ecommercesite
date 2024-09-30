from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request,  'contact.html')

def fruit(request):
    return render(request, 'fruit.html')

def testimonial(request):
    return render (request,'testimonial.html')