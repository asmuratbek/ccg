from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'base.html')

def contacts(request):
    return render(request, 'contacts.html')

def portfolio_inner(request):
    return render(request, 'portfolio-inner.html')

def about(request):
    return render(request, 'about.html')

