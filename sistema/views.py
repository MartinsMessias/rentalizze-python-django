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
            if not q1 or not q2:

                form.save()
                messages.success(request, 'Cliente cadastrado com sucesso!')
                return redirect(listar_clientes)

            else:
                messages.warning(request, "Cpf ou Cnpj ja existe!")
                return render(request, 'sistema/cadastrar_cliente.html', {'form': form})
    form = ClienteForm()

    # Fazer verificação pra n permitir CPF e CNPJ duplicados

    return render(request, 'sistema/cadastrar_cliente.html', {'form': form})

def listar_clientes(request):
    dados = Cliente.objects.all().order_by('criado_em')
    return render(request, 'sistema/listar_clientes.html', {'dados':dados})


def editar_cliente(request, id):
    form = {}
    #cliente = Cliente.objects.get.(id=id)
   # form = ClienteForm(request.POST or None, instance=Cliente)
    #if form.is_valid():
       # form.save()
      #  messages.success(request, "Cliente modificado com sucesso!")
     #   return redirect()


    return render(request, 'sistema/editar_cliente.html', {'form': form})
############# FIM CLIENTE #################


############# VEÍCULO #################
def cadastrar_veiculo(request):###################################################
    if request.method =='POST':## DEIXAR NO MESMO FORMATO DA CADASTRAR CLIENTE ##
        form = AutomovelForm(request.POST)#######################################

        if form.is_valid():
            form.save()
            messages.success(request, 'Veiculo cadastrado com sucesso!')
            return redirect(listar_veiculos)
        else:
            messages.warning(request, 'Houve um erro! {}'.format(form.errors))
    form = AutomovelForm()

    # Fazer verificação pra não permitir duplicados (com a mesma placa)

    return render(request, 'sistema/cadastrar_veiculo.html', {'form':form})

def listar_veiculos(request):
    dados = Automovel.objects.all().order_by('criado_em')

    return render(request, 'sistema/listar_veiculos.html', {'dados':dados})


def editar_veiculo(request, id):
    dados = {}
    return render(request, 'sistema/editar_veiculo.html', {'dados': dados})

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
            messages.warning(request, 'Houve um erro {}'.format(form.errors))
    form = LocacaoForm()

    return render(request, 'sistema/reserva.html', {'form':form})

def listar_locacoes(request):
    dados = Locacao.objects.all().orde_by('criado_em')
    return render(request, 'sistema/listar_reservas.html', {'dados':dados})

def editar_loc(request, id):
    dados = {}
    return render(request, 'sistema/editar_locacao.html', {'dados': dados})

############# FIM LOCAÇÃO #################

