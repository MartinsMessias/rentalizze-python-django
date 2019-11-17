from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


# Renderiza a página inicial
@login_required
def index(request):
    return render(request, 'sistema/index.html', locals())


############# CLIENTE #################
@login_required
def cadastrar_cliente(request):
    if request.method =='POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect(listar_clientes)

        messages.warning(request, 'Houve um erro!')
        return render(request, 'sistema/cadastrar_cliente.html', {'form': form})

    form = ClienteForm()
    return render(request, 'sistema/cadastrar_cliente.html', {'form': form})

@login_required
def listar_clientes(request):
    dados = Cliente.objects.all().order_by('criado_em')
    return render(request, 'sistema/listar_clientes.html', {'dados':dados})

@login_required
def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        messages.success(request, "Cliente modificado com sucesso!")
        return redirect(listar_clientes)

    return render(request, 'sistema/editar_cliente.html', {'form': form})

@login_required
def excluir_cliente(request, id):
    cliente = Cliente.objects.get(id=id)

    # Não deixa um cliente ser excluído caso esteja em uma locação
    if Locacao.objects.filter(cliente_id=cliente.id):
        messages.warning(request, "Não é possível excluir o cliente! Está em uma locação!")
        return redirect(listar_clientes)

    cliente.delete()
    messages.success(request, "Cliente excluído com sucesso!")
    return redirect(listar_clientes)
############# FIM CLIENTE #################


############# VEÍCULO #################
@login_required
def cadastrar_veiculo(request):
    if request.method =='POST':
        form = AutomovelForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo cadastrado com sucesso!')
            return redirect(listar_veiculos)

        messages.warning(request, 'Houve um erro!')
        return render(request, 'sistema/cadastrar_veiculo.html', {'form': form})

    form = AutomovelForm()
    return render(request, 'sistema/cadastrar_veiculo.html', {'form':form})

@login_required
def listar_veiculos(request):
    dados = Automovel.objects.all().order_by('criado_em')
    return render(request, 'sistema/listar_veiculos.html', {'dados':dados})

@login_required
def editar_veiculo(request, id):
    automovel = Automovel.objects.get(id=id)
    form = AutomovelForm(request.POST or None, instance=automovel)

    if form.is_valid():
        form.save()
        messages.success(request, "Veiculo modificado com sucesso!")
        return redirect(listar_veiculos)

    return render(request, 'sistema/editar_veiculo.html', {'form': form})

@login_required
def excluir_automovel(request, id):
    automovel = Automovel.objects.get(id=id)

    # Não deixa um veículo ser excluído caso esteja em uma locação
    if Locacao.objects.filter(carro_id=automovel.id):
        messages.warning(request, "Não é possível excluir o automóvel! Está em uma locação!")
        return redirect(listar_veiculos)

    automovel.delete()
    messages.success(request, "Automóvel excluído com sucesso!")
    return redirect(listar_veiculos)

@login_required
def listar_auto_locados(request):
    dados = Locacao.objects.filter(carro__status='Indisponível').order_by('data_locacao')
    return render(request, 'sistema/lista_locados.html', {'dados': dados})

############# FIM VEÍCULO #################

############# LOCAÇÃO #################
@login_required
def locar_veiculo(request):
    if request.method =='POST':
        form = LocacaoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Locação realizada com sucesso!')
            return redirect(listar_locacoes)
        msg = 'Houve um erro!' + str(form.errors)
        messages.warning(request, msg)
        return render(request, 'sistema/reserva.html', {'form':form})

    form = LocacaoForm()
    return render(request, 'sistema/reserva.html', {'form':form})

@login_required
def listar_locacoes(request):
    dados = Locacao.objects.filter(status='Ativo').order_by('criado_em')
    return render(request, 'sistema/listar_reservas.html', {'dados':dados})

@login_required
def historico_locacoes(request):
    dados = Locacao.objects.filter(status='Inativo').order_by('criado_em')
    return render(request, 'sistema/listar_reservas.html', {'dados':dados})

@login_required
def editar_loc(request, id):
    locacao = Locacao.objects.get(id=id)
    form = EditLocacaoForm(request.POST or None, instance=locacao)

    if form.is_valid():
        form.save()
        messages.success(request, "Locação modificada com sucesso!")
        return redirect(listar_locacoes)

    return render(request, 'sistema/editar_locacao.html', {'form': form})

@login_required
def excluir_loc(request, id):
    locacao = Locacao.objects.get(id=id)

    # Antes de excluír, altera o status do automóvel
    carro = Automovel.objects.get(id=locacao.carro.id)
    carro.status = 'Disponível'
    carro.save()

    locacao.delete()
    messages.success(request, "Locação excluída com sucesso")
    return redirect(listar_locacoes)

@login_required
def finalizar_loc(request, id):
    dados = Locacao.objects.get(id=id)
    form = FimLocacaoForm()

    if form.is_valid():
        dados.valor_locacao += form.cleaned_data['valor_adicional']
        form.save(commit=False)

    if request.method == 'POST':
        form = FimLocacaoForm(request.POST)

        if form.is_valid():
            carro = Automovel.objects.get(id=dados.carro.id)
            carro.status = 'Disponível'
            carro.quilometragem_automovel += form.cleaned_data['quilometragem']
            carro.save()
            locacao = Locacao.objects.get(id=dados.id)
            locacao.status = 'Inativo'
            messages.success(request, "Locação finalizada com sucesso!")
            return redirect(listar_locacoes)

    return render(request, 'sistema/fim_locacao.html', {'dados': dados,'form':form})
############# FIM LOCAÇÃO #################


############# USUÁRIO E CONTAS #################
# Modificação de senha
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Atualiza o hash da sessão
            messages.success(request, 'Sua senha foi atualizada com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Houve um erro!.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})

# Mostra informações básicas do usuário atual
@login_required
def perfil(request):
    dados = User.objects.get(username__iexact=request.user.username)
    return render(request, 'registration/perfil.html', {'form': dados})

# Lista todos usuários do sistema
@login_required
def listar_users(request):
    dados = User.objects.all()
    return render(request, 'registration/allusers.html', {'dados': dados})

# Retorna 404 para /accounts/
@login_required
def accounts(request):
    return HttpResponse(404)
