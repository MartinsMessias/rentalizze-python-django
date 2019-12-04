from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import *

# Renderiza a página inicial
@login_required
def index(request):
    data = date.today()

    clientes = Cliente.objects.all()

    carros = Automovel.objects.all()
    carros_ativos = Automovel.objects.filter(status='Indisponível')

    locacoes = Locacao.objects.all()
    locacoes_ativas = Locacao.objects.filter(status='Ativo')

    receita = Locacao.objects.filter(status='Inativo').aggregate(valor_locacao=Sum('valor_locacao')).get('valor_locacao')
    receita_andamento = Locacao.objects.filter(status='Ativo').aggregate(valor_locacao=Sum('valor_locacao')).get('valor_locacao')

    return render(request, 'sistema/index.html', locals())


############# CLIENTE #################
# Cadastra cliente
@login_required  # <<< requer login para acessar essa view
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

# Lista todos os clientes
@login_required
def listar_clientes(request):
    dados = Cliente.objects.all().order_by('-criado_em')
    return render(request, 'sistema/listar_clientes.html', {'dados':dados})

# Edita dados do cliente específico
@login_required
def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        messages.success(request, "Cliente modificado com sucesso!")
        return redirect(listar_clientes)

    return render(request, 'sistema/editar_cliente.html', {'form': form})

# Excluí um cliente que não está em uma locação
@login_required
def excluir_cliente(request, id):
    cliente = Cliente.objects.get(id=id)

    # Não deixa um cliente ser excluído caso esteja em uma locação
    # Filtra os ID para verificar se existe Locação com o cliente
    if Locacao.objects.filter(cliente_id=cliente.id):
        messages.warning(request, "Não é possível excluir o cliente! Está em uma locação!")
        return redirect(listar_clientes)

    cliente.delete()
    messages.success(request, "Cliente excluído com sucesso!")
    return redirect(listar_clientes)

# Lista dados de locações que já passaram
@login_required
def historico_cliente(request, id):
    dados = Locacao.objects.filter(status='Inativo', cliente_id=id).order_by('criado_em').reverse()
    return render(request, 'sistema/listar_reservas.html', {'dados':dados})

############# FIM CLIENTE #################


############# VEÍCULO #################
# Cadastra um automóvel
@login_required
def cadastrar_veiculo(request):
    if request.method =='POST':
        form = AutomovelForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo cadastrado com sucesso!')
            return redirect(listar_veiculos)

        # Caso o form seja inválido
        messages.warning(request, 'Houve um erro!')
        return render(request, 'sistema/cadastrar_veiculo.html', {'form': form})

    form = AutomovelForm()
    return render(request, 'sistema/cadastrar_veiculo.html', {'form':form})

# Lista todos os automóveis
@login_required
def listar_veiculos(request):
    dados = Automovel.objects.all().order_by('criado_em').reverse()
    return render(request, 'sistema/listar_veiculos.html', {'dados':dados})

# Edita dados do auto
@login_required
def editar_veiculo(request, id):
    automovel = Automovel.objects.get(id=id)
    form = AutomovelForm(request.POST or None, instance=automovel)

    if form.is_valid():
        form.save()
        messages.success(request, "Veiculo modificado com sucesso!")
        return redirect(listar_veiculos)

    return render(request, 'sistema/editar_veiculo.html', {'form': form})

# Excluí um auto que não esteja em locação
@login_required
def excluir_automovel(request, id):
    automovel = Automovel.objects.get(id=id)

    # Não deixa um veículo ser excluído caso esteja em uma locação
    # Filtra nos ID para verificar se o carro está em uma locação
    if Locacao.objects.filter(carro_id=automovel.id):
        messages.warning(request, "Não é possível excluir o automóvel! Está em uma locação!")
        return redirect(listar_veiculos)

    automovel.delete()
    messages.success(request, "Automóvel excluído com sucesso!")
    return redirect(listar_veiculos)

# Lista dados de locações que já passaram com esse carro
@login_required
def historico_veiculo(request, id):
    #Locações finalizadas recebem o status de 'Inativo'
    dados = Locacao.objects.filter(status='Inativo', carro_id=id).order_by('-criado_em')
    return render(request, 'sistema/listar_reservas.html', {'dados':dados})

############# FIM VEÍCULO #################

############# LOCAÇÃO #################
# Realiza locação
@login_required
def locar_veiculo(request):
    if request.method =='POST':
        form = LocacaoForm(request.POST)

        if form.is_valid():
            form.save()

            # Altera status do automóvel locado
            carro = Automovel.objects.get(id=int(request.POST.get('carro'))) # Pega ID do <select>
            carro.status = 'Indisponível'
            carro.save()

            messages.success(request, 'Locação realizada com sucesso!')
            return redirect(listar_locacoes)

        messages.warning(request, 'Houve um erro!')
        return render(request, 'sistema/reserva.html', {'form':form})

    form = LocacaoForm()
    return render(request, 'sistema/reserva.html', {'form':form})

# Lista todas as locações
@login_required
def listar_locacoes(request):
    dados = Locacao.objects.filter(status='Ativo').order_by('-criado_em')
    return render(request, 'sistema/listar_reservas.html', {'dados':dados})

# Lista locações que já passaram
@login_required
def historico_locacoes(request):
    dados = Locacao.objects.filter(status='Inativo').order_by('-criado_em')
    return render(request, 'sistema/listar_reservas.html', {'dados':dados, 'fim':True})

# Edita locação específica
@login_required
def editar_loc(request, id):
    locacao = Locacao.objects.get(id=id)
    form = EditLocacaoForm(request.POST or None, instance=locacao)

    if form.is_valid():
        form.save()
        messages.success(request, "Locação modificada com sucesso!")
        return redirect(listar_locacoes)

    return render(request, 'sistema/editar_locacao.html', {'form': form})

# Excluí locação
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

# Realiza a devolução do automóvel
@login_required
def finalizar_loc(request, id):
    # Essa var 'dados' só vai ser usada no template
    dados = Locacao.objects.get(id=id)

    if request.method == 'POST':
        form = FimLocacaoForm(request.POST)

        if form.is_valid():

            # Locações finalizadas recebem o status de 'Inativo'
            locacao = Locacao.objects.get(id=dados.id)
            locacao.status = 'Inativo'

            # Depois de passar pelo 'is_valid()' os dados do form estarão em 'form.cleaned_data[]'
            # Significa que os dados estão 'limpos' e em formato Python.

            # Substituimos o valor salvo pelo valor recebido do formulário
            locacao.valor_locacao = form.cleaned_data['valor_locacao_f']    # Caso o valor final seja alterado
            locacao.data_devolucao = form.cleaned_data['data_devolucao_f']  # Caso a data seja alterada

            # Altera dados(status, km) do automóvel após a finalização de locação
            carro = Automovel.objects.get(id=dados.carro.id)
            carro.status = 'Disponível' # Após o fim da locação o carro está disponível novamente
            carro.quilometragem_automovel = form.cleaned_data['quilometragem'] # Adiciona km ao veículo

            # Salva
            carro.save()
            locacao.save()

            messages.success(request, "Locação finalizada com sucesso!")
            return redirect(listar_locacoes)

    form = FimLocacaoForm()
    return render(request, 'sistema/fim_locacao.html', {'dados': dados,'form':form})
############# FIM LOCAÇÃO #################


############# USUÁRIO E CONTAS #################
# Modificação de senha do usuário atual
@login_required
def change_password(request):
    if request.method == 'POST':
        # Envia para o form os dados do 'POST' e da instância do usuário atual
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Atualiza o hash da sessão
            messages.success(request, 'Sua senha foi atualizada com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Houve um erro!')

    form = PasswordChangeForm(request.user) # Envia para o template os dados da instância do usuário atual
    return render(request, 'registration/change_password.html', {'form': form})

# Mostra informações do usuário
@login_required
def perfil(request):
    dados = User.objects.get(id=request.user.id)
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
