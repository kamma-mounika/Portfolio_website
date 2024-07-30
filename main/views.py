from django.shortcuts import render
from django.conf import settings

def index(request):
    context = {
        "name": settings.DATA["NAME"],
        "about_me": settings.DATA["ABOUT_ME"]
        }  # Add context if needed
    return render(request, 'main/index.html', context)

def projects(request):
    context = {}  # Add context if needed
    return render(request, 'main/projects.html', context)

def languages(request):
    context = {}  # Add context if needed
    return render(request, 'main/languages.html', context)

def certifications(request):
    context = {}  # Add context if needed
    return render(request, 'main/certifications.html', context)

def contact(request):
    context = {}  # Add context if needed
    return render(request, 'main/contact.html', context)





