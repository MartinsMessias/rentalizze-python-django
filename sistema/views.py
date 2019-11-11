from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


def index(request):
    return render(request, 'sistema/index.html', locals())

@login_required
def cadastrar_cliente(request):
    form = ClienteForm()
    #########################################################
    # Fazer o código de salvar o cliente no banco de dados #
    ########################################################
    return render(request, 'sistema/cadastrar_cliente.html', {'form': form})

@login_required
def cadastrar_veiculo(request):
    form = AutomovelForm()
    # ###################################################### #
    # Fazer o código de salvar o automóvel no banco de dados #
    # ###################################################### #
    return render(request, 'sistema/cadastrar_veiculo.html', {'form':form})

@login_required
def locar_veiculo(request):
    form = LocacaoForm()
    # ###################################################### #
    # Fazer o código de salvar a locação no banco de dados  #
    # ###################################################### #
    return render(request, 'sistema/reserva.html', {'form':form})

@login_required
def listar_reservas(request):
    dados = 1
    # ###################################################### #
    # Fazer o código para enviar todos os objetos de Locacao #
    # ###################################################### #
    return render(request, 'sistema/listar_reservas.html', {'dados':dados})

@login_required
def visualizar_loc(request, id):
    dados = 1 # Mandar para essa variável os objetos com "id" igual ao que foi pedido
    # ################################################################## #
    # Fazer o código para enviar o objeto de Locacao com o id que pede ###
    # ################################################################## #
    return render(request, 'sistema/vizualizar_loc.html', {'dados':dados})
