from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


def index(request):
    return render(request, 'sistema/index.html', locals())


def cadastrar_cliente(request):
    form = ClienteForm()

    #########################################################
    # Fazer o código de salvar o cliente no banco de dados #
    ########################################################

    return render(request, 'sistema/cadastrar_cliente.html', {'form': form})


def cadastrar_veiculo(request):
    form = AutomovelForm()
    # ###################################################### #
    # Fazer o código de salvar o automóvel no banco de dados #
    # ###################################################### #
    return render(request, 'sistema/cadastrar_veiculo.html', {'form':form})
