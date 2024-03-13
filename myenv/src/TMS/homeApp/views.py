from django.shortcuts import render

def aboutView(request):
    return render(request, 'About.html')

def contactView(request):
    return render(request, 'Contact.html')

def homeView(request):
    return render(request, 'Home.html')

# Create your views here.
