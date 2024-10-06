from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')


# def billing(request):
#
#     # Page from the theme
#     return render(request, 'pages/billing.html')


def profile(request):

    # Page from the theme
    return render(request, 'pages/profile.html')


def tables(request):

    # Page from the theme
    return render(request, 'pages/tables.html')


def virtualreality(request):

    # Page from the theme
    return render(request, 'pages/virtual-reality.html')


def rtl(request):

    # Page from the theme
    return render(request, 'pages/rtl.html')
