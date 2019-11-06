from django.http import HttpResponse
from django.shortcuts import render, redirect
from pyUFbr import baseuf
from .forms import *


#################################################
# As views de CADASTRAR_... devem enviar o form para o template
# As views de CADASTRAR_... devem realizar o salvamento das informações recebidas pelo template
#################################################

def index(request):
    return render(request, 'sistema/index.html', locals())


def cadastrar_cliente(request):
    em = baseuf.ufbr.list_uf
    form = ClienteForm()
    #########################################################
    # Fazer o código de salvar o cliente no banco de dados #
    ########################################################
    return render(request, 'sistema/cadastrar_cliente.html', {'form': form, 'em': em})


def cadastrar_veiculo(request):
    form = AutomovelForm()
    # ###################################################### #
    # Fazer o código de salvar o automóvel no banco de dados #
    # ###################################################### #
    return render(request, 'sistema/cadastrar_veiculo.html', {'form':form})
