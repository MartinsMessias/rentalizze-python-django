from django.http import HttpResponse
from django.shortcuts import render
from pyUFbr import *
from .forms import *

#################################################
# As views de CADASTRAR_... devem enviar o form para o template
# As views de CADASTRAR_... devem realizar o salvamento das informações recebidas pelo template
#################################################

def index(request):
    titulo_pagina = {'page': 'Homepage'}
    return render(request, 'sistema/index.html', locals())

def cadastrar_cliente(request):
    form = ClienteForm()
    estados = ufbr.list_uf()
    print(estados)
    titulo_pagina = {'page': 'Cadastro de cliente'}
    return render(request, 'sistema/cadastrar_cliente.html', locals())

def cadastrar_veiculo(request):
    # form = Envie para essa variavel o VeiculoForm
    titulo_pagina = {'page': 'Cadastro de veículo'}
    return render(request, 'sistema/cadastrar_veiculo.html', locals())

