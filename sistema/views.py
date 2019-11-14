from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *

# Renderiza a página inicial
def index(request):
    return render(request, 'sistema/index.html', locals())


############# CLIENTE #################
def cadastrar_cliente(request):
    if request.method =='POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect(listar_clientes)
        else:
            messages.warning(request, 'Houve um erro! {}'.format(form.errors))

    form = ClienteForm()

    # Fazer verificação pra n permitir CPF e CNPJ duplicados

    return render(request, 'sistema/cadastrar_cliente.html', {'form': form})

def listar_clientes(request):#########################################
    dados = Cliente.objects.all() # Ordenar por 'criado_em'###########
    return render(request, 'sistema/listar_clientes.html', {'dados':dados})


def visualizar_cliente(request, id):
    dados = {}
    #########################################################
    # Mandar para a variável 'dados' o cliente cujo o id=id #
    #########################################################
    return render(request, 'sistema/visualizar_cli.html', {'dados':dados})
############# FIM CLIENTE #################


############# VEÍCULO #################
def cadastrar_veiculo(request):###################################################
    if request.method =='POST':## DEIXAR NO MESMO FORMATO DA CADASTRAR CLIENTE ##
        form = AutomovelForm(request.POST)#######################################
        if form.is_valid():
            form.save()
            return redirect(listar_veiculos)
    else:
        form = AutomovelForm()

    # Fazer verificação pra não permitir duplicados (com a mesma placa)

    return render(request, 'sistema/cadastrar_veiculo.html', {'form':form})

def listar_veiculos(request):
    dados = {}
    #########################################################
    # Mandar para a variável 'dados' todos os veículos (all)#
    #########################################################
    return render(request, 'sistema/listar_veiculos.html', {'dados':dados})


def editar_veiculo(request, id):
    pass

############# FIM VEÍCULO #################

############# LOCAÇÃO #################
def locar_veiculo(request):############################################## #
    if request.method =='POST':### DEIXAR NO FORMATO DA CADASTRAR CLIENTE #
        form = LocacaoForm(request.POST)################################# #
        if form.is_valid():
            form.save()
            return redirect(listar_locacoes)
    else:
        form = LocacaoForm()

    return render(request, 'sistema/reserva.html', {'form':form})

def listar_locacoes(request):
    dados = Locacao.objects.all()
    return render(request, 'sistema/listar_reservas.html', {'dados':dados})

def editar_loc(request, id):
    pass
############# FIM LOCAÇÃO #################

