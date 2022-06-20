from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse('<h1>first text</h1>')

def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')
