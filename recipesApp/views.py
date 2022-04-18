from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Junio'
    })

def about(request):
    return HttpResponse(request, 'recipes/about.html',)

def contact(request):
    return render(request, 'recipes/contact.html')
