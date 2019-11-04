from django.http import HttpResponse
from django.shortcuts import render


def teste(request):
    test = {'page': 'Homepage'}
    return render(request, 'sistema/index.html', {'test': test})


def cadastrar_cliente(request):
    # TEST
    test = {'page': 'Cadastro de cliente'}
    return render(request, 'sistema/cadastrar_cliente.html', {'test': test})
