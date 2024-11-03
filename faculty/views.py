from django.shortcuts import render

# Create your views here.


def engineer(request):
    return render(request, "faculty/engineer.html")

def health(request):
    return render(request, "faculty/health.html")
