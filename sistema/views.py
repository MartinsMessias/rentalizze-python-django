from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


def index(request):
    return render(request, 'sistema/index.html', locals())

def cadastrar_cliente(request):
    form = ClienteForm()
    if request.method =='POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(cadastrar_cliente)
    else:
        form = ClienteForm()
    #########################################################
    # Fazer o código de salvar o cliente no banco de dados #
    ########################################################
    return render(request, 'sistema/cadastrar_cliente.html', {'form': form})

def listar_clientes(request):
    dados = Cliente.objects.all()
    return render(request, 'sistema/listar_clientes.html', {'dados':dados})

def cadastrar_veiculo(request):
    form = AutomovelForm()
    if request.method =='POST':
        form = AutomovelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(cadastrar_veiculo)
    else:
        form = AutomovelForm()
    # ###################################################### #
    # Fazer o código de salvar o automóvel no banco de dados #
    # ###################################################### #
    return render(request, 'sistema/cadastrar_veiculo.html', {'form':form})

def locar_veiculo(request):
    form = LocacaoForm()

    # ###################################################### #
    # Fazer o código de salvar a locação no banco de dados  #
    # ###################################################### #
    return render(request, 'sistema/reserva.html', {'form':form})

def listar_reservas(request):
    dados = Locacao.objects.all()
    return render(request, 'sistema/listar_reservas.html', {'dados':dados})

def visualizar_loc(request, id):
    dados = Locacao.objects.get(id=id)
    return render(request, 'sistema/vizualizar_loc.html', {'dados':dados})


