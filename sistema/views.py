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
            q1 = Cliente.objects.filter(cpf_cliente=form.cleaned_data['cpf_cliente'])
            q2 = Cliente.objects.filter(cnpj_cliente=form.cleaned_data['cnpj_cliente'])

            if not q1:
                form.save()
                messages.success(request, 'Cliente cadastrado com sucesso!')
                return redirect(listar_clientes)

            if not q2:
                form.save()
                messages.success(request, 'Cliente cadastrado com sucesso!')
                return redirect(listar_clientes)

            messages.warning(request, "Já existe um cliente com este CPF/CNPJ!")
            return render(request, 'sistema/cadastrar_cliente.html', {'form': form})

    form = ClienteForm()
    return render(request, 'sistema/cadastrar_cliente.html', {'form': form})

def listar_clientes(request):
    dados = Cliente.objects.all().order_by('criado_em')
    return render(request, 'sistema/listar_clientes.html', {'dados':dados})


def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        messages.success(request, "Cliente modificado com sucesso!")
        return redirect(listar_clientes)

    return render(request, 'sistema/editar_cliente.html', {'form': form})

def excluir_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    messages.success(request, "Cliente excluído com sucesso!")
    return redirect(listar_clientes)
############# FIM CLIENTE #################


############# VEÍCULO #################
def cadastrar_veiculo(request):
    if request.method =='POST':
        form = AutomovelForm(request.POST)

        if form.is_valid():
            q1 = Automovel.objects.filter(placa_automovel=form.cleaned_data['placa_automovel'])
            if not q1:
                form.save()
                messages.success(request, 'Veículo cadastrado com sucesso!')
                return redirect(listar_veiculos)
            else:
                messages.warning(request, 'Houve um erro, placa já cadastrada!')

    form = AutomovelForm()

    return render(request, 'sistema/cadastrar_veiculo.html', {'form':form})

def listar_veiculos(request):
    dados = Automovel.objects.all().order_by('criado_em')
    return render(request, 'sistema/listar_veiculos.html', {'dados':dados})


def editar_veiculo(request, id):
    automovel = Automovel.objects.get(id=id)
    form = AutomovelForm(request.POST or None, instance=automovel)

    if form.is_valid():
        form.save()
        messages.success(request, "Veiculo modificado com sucesso!")
        return redirect(listar_veiculos)

    return render(request, 'sistema/editar_veiculo.html', {'form': form})

def excluir_automovel(request, id):
    automovel = Automovel.objects.get(id=id)
    automovel.delete()
    messages.success(request, "Automovel excluído com sucesso")
    return redirect(listar_veiculos)
############# FIM VEÍCULO #################

############# LOCAÇÃO #################
def locar_veiculo(request):
    if request.method =='POST':
        form = LocacaoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Locação realizada com sucesso!')
            return redirect(listar_locacoes)
        else:
            messages.warning(request, 'Houve um erro!')

    form = LocacaoForm()
    return render(request, 'sistema/reserva.html', {'form':form})

def listar_locacoes(request):
    dados = Locacao.objects.all().order_by('criado_em')
    return render(request, 'sistema/listar_reservas.html', {'dados':dados})

def editar_loc(request, id):
    locacao = Locacao.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=locacao)

    if form.is_valid():
        form.save()
        messages.success(request, "Locação modificada com sucesso!")
        return redirect(listar_locacoes)

    return render(request, 'sistema/editar_locacao.html', {'form': form})


def excluir_loc(request, id):
    locaçao = Locacao.objects.get(id=id)
    locaçao.delete()
    messages.success(request, "Locação excluída com sucesso!")
    return redirect(listar_locacoes)
############# FIM LOCAÇÃO #################

