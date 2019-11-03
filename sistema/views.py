from django.http import HttpResponse
from django.shortcuts import render

def teste(request):
    test = {'page': 'Homepage', 'desc':'Página inicial'}
    return render(request, 'sistema/index.html', {'test': test})
