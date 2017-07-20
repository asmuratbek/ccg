from django.shortcuts import render

# Create your views here.
from about.models import AboutUs
from portfolio.models import Portfolio


def index(request):
    _portfolio = Portfolio.objects.all().order_by('-created_at')
    _about = AboutUs.objects.all()

    context = {
        'portfolio': _portfolio,
        'about': _about,
    }

    return render(request, 'index.html', context)


def portfolio(request):
    _portfolio = Portfolio.objects.all().order_by('-created_at')

    context = {
        'portfolio': _portfolio
    }

    return render(request, 'portfolio.html', context)


def contacts(request):
    return render(request, 'contacts.html')


def portfolio_inner(request, id):
    _portfolio = Portfolio.objects.get(id=id)

    context = {
        'portfolio': _portfolio
    }
    return render(request, 'portfolio-inner.html', context)


def about(request):
    return render(request, 'about.html')
