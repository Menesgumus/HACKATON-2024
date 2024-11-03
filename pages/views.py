from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    return render(request, "pages/homepage.html")

def contact(request):
    return render(request, "pages/contact.html")

def education(request):
    return render(request, "pages/education.html")

def about(request):
    return render(request, "pages/about.html")