import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Cliente(models.Model):
    STATUS_CHOICES = (('Ativo', 'Ativo'), ('Inativo', 'Inativo'))
    nome_cliente = models.CharField(max_length=200)
    cpf_cliente = models.CharField(max_length=14, unique=True, null=True, blank=True)
    telefone_cliente = models.CharField(max_length=20)
    email_cliente = models.CharField(max_length=120)
    rg_cliente = models.CharField(max_length=50)
    cnpj_cliente = models.CharField(max_length=50, unique=True, blank=True, null=True)
    cnh_cliente = models.CharField(max_length=100)
    validade_cnh = models.DateField(max_length=50)
    criado_em = models.DateTimeField(auto_now=True)
    rua = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=200, default='SEM', blank=True)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=200)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=200)
    modificado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)

    def __str__(self):
        return self.nome_cliente + ' - ' + self.status

    def save(self, *args, **kwargs):
        if not self.cpf_cliente:
            self.cpf_cliente = None
        else:
            self.cnpj_cliente = None
        super(Cliente, self).save(*args, **kwargs)

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
        ('Indisponível', 'Indisponível'),
    )
    COMBUSTIVEL_CHOICES = (
        ('Gasolina', 'Gasolina'), ('Flex', 'Flex'),
        ('Diesel', 'Diesel'), ('Híbrido/Elétrico', 'Híbrido/Elétrico'),
    )
    MARCA_CHOICES = (
        ('Mercedes - Benz', 'Mercedes - Benz'), ('Audi', 'Audi'),('BMW', 'BMW'),
        ('Volkswagen',  'Volkswagen'), ('Chevrolet', 'Chevrolet'), ('Renault', 'Renault'),
        ('Ford', 'Ford'), ('Toyota', 'Toyota'), ('Fiat', 'Fiat'), ('Hyundai', 'Hyundai'),
        ('Peugeot', 'Peugeot'), ('Lexus', 'Lexus'), ('Kia','Kia'), ('Citroën', 'Citroën'),
        ('Nissan', 'Nissan'), ('Mitsubishi', 'Mitsubishi'), ('Chery', 'Chery'),('Jeep', 'Jeep'),
    )
    CATEGORIA_CHOICES = (
        ('Utilitário Esportivo', 'Utilitário Esportivo'),
        ('Sedã', 'Sedã'), ('Conversível / Cupê', 'Conversível / Cupê'),
        ('Hatch', 'Hatch'), ('Picape', 'Picape'), ('Hibrido / Elétrico', 'Hibrido / Elétrico'),
        ('Van','Van'), ('Outro', 'Outro'),
    )

    NRO_PORTAS_AUTOMOVEL_CHOICES =(
        ('2', '2 Portas'),
        ('3', '3 Portas'),
        ('4', '4 Portas'),
        ('5', '5 Portas'),
    )
    placa_automovel = models.CharField(max_length=15, unique=True, error_messages={'unique':"Já há um automóvel com esta placa!"})
    cor_automovel = models.CharField(max_length=20)
    nro_portas_automovel = models.CharField(max_length=10, choices=NRO_PORTAS_AUTOMOVEL_CHOICES)
    tipo_combustivel_automovel = models.CharField(max_length=50, choices=COMBUSTIVEL_CHOICES)
    quilometragem_automovel = models.FloatField()
    chassi_automovel = models.IntegerField(unique=True)
    valor_locacao = models.FloatField()
    valor_locacao_fds = models.FloatField()
    motor = models.CharField(max_length=3)
    marca = models.CharField(choices=MARCA_CHOICES, max_length=50)
    modelo = models.CharField(max_length=200)
    ano = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year)])
    criado_em = models.DateTimeField(auto_now=True)
    categoria = models.CharField(choices=CATEGORIA_CHOICES, max_length=50)
    modificacado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)


    def __str__(self):
        return self.marca +' '+ self.modelo +' '+ str(self.ano) +' - '+ self.status
