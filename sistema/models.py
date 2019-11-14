import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Cliente(models.Model):
    STATUS_CHOICES = (('Ativo', 'Ativo'), ('Inativo', 'Inativo'))
    nome_cliente = models.CharField(max_length=200)
    cpf_cliente = models.CharField(max_length=20, default='---')
    telefone_cliente = models.CharField(max_length=20)
    email_cliente = models.CharField(max_length=120)
    rg_cliente = models.CharField(max_length=50)
    cnpj_cliente = models.CharField(max_length=50, default='---')
    cnh_cliente = models.CharField(max_length=100)
    validade_cnh = models.DateField(max_length=50)
    criado_em = models.DateTimeField(auto_now=True)
    rua = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=200, default='SEM')
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=200)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=200)
    modificado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)

    def __str__(self):
        return self.nome_cliente

class Locacao(models.Model):
    TIPO_CHOICES = (('Reserva', 'Reserva'), ('Saída', 'Saída'))
    hora_locacao = models.TimeField()
    data_locacao = models.DateField()
    hora_devolucao = models.TimeField()
    data_devolucao = models.DateField()
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    carro = models.ForeignKey('Automovel', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now=True)
    modificacado_em = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)

    def __str__(self):
        inicio, fim = str(self.data_locacao), str(self.data_devolucao)
        return self.cliente.nome_cliente + ' | ' + inicio + '/' + fim


class Automovel(models.Model):
    STATUS_CHOICES = (
        ('Disponível', 'Disponível'),
        ('Indisponível', 'Indisponível')
    )
    COMBUSTIVEL_CHOICES = (
        ('Gasolina AD', 'Gasolina AD'),
        ('Gasolina C', 'Gasolina C'),
        ('Etanol', 'Etanol'),
        ('Diesel', 'Diesel'),
        ('GNV', 'Gás GNV'),
        ('Álcool', 'Álcool'),
        ('Elétrico/Outro', 'Elétrico/Outro'),
    )
    placa_automovel = models.CharField(max_length=15)
    cor_automovel = models.CharField(max_length=20)
    nro_portas_automovel = models.IntegerField()
    tipo_combustivel_automovel = models.CharField(max_length=20, choices=COMBUSTIVEL_CHOICES)
    quilometragem_automovel = models.FloatField()
    chassi_automovel = models.IntegerField()
    valor_locacao = models.DecimalField(max_digits=6, decimal_places=2)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    ano = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year)])
    criado_em = models.DateTimeField(auto_now=True)
    categoria = models.CharField(max_length=200)
    modificacado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)


    def __str__(self):
        return self.modelo
