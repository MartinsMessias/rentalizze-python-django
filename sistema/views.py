from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

#
def index(request):
    return render(request, 'sistema/index.html', locals())

####### CLIENTE
def cadastrar_cliente(request):
    if request.method =='POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listar_clientes)
    else:
        form = ClienteForm()
    return render(request, 'sistema/cadastrar_cliente.html', {'form': form})

def listar_clientes(request):
    dados = Cliente.objects.all()
    return render(request, 'sistema/listar_clientes.html', {'dados':dados})
###### FIM CLIENTE

####### VEÍCULO
def cadastrar_veiculo(request):
    if request.method =='POST':
        form = AutomovelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listar_veiculos)
    else:
        form = AutomovelForm()

    return render(request, 'sistema/cadastrar_veiculo.html', {'form':form})

def listar_veiculos(request):

    return render(request, 'sistema/listar_veiculos.html')


####### FIM VEÍCULO
def locar_veiculo(request):
    if request.method =='POST':
        form = LocacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listar_locacoes)
    else:
        form = LocacaoForm()

    return render(request, 'sistema/reserva.html', {'form':form})

def listar_locacoes(request):
    dados = Locacao.objects.all()

    return render(request, 'sistema/listar_reservas.html', {'dados':dados})

def visualizar_loc(request, id):
    dados = Locacao.objects.get(id=id)

    return render(request, 'sistema/vizualizar_loc.html', {'dados':dados})


