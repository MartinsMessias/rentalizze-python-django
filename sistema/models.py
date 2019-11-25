from django.db import models
from django.contrib.auth.models import User # Importa tabela de usuários do Django
from django_currentuser.db.models import CurrentUserField # Campo do Usuário atual

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
        if self.cpf_cliente:
            return self.nome_cliente + ' - ' + self.cpf_cliente
        return self.nome_cliente + ' - ' + self.cnpj_cliente

    # Esse método vai ser executado toda vez que der um .save() em Cliente em views.py
    # Aqui foi configurado para permitir um cliente ser salvo com CPF ou CNPJ vazios.
    # Foi necessário pois os campos CPF e CNPJ estão com UNIQUE=True, porem não permitia 2 ou + clientes com CPF vázios
    def save(self, *args, **kwargs):
        # Deve permitir salvar um cliente com o CPF ou o CPNJ vazio. Não os dois.
        if not self.cpf_cliente:
            self.cpf_cliente = None
        else:
            self.cnpj_cliente = None

        super(Cliente, self).save(*args, **kwargs)


class Locacao(models.Model):
    STATUS_CHOICES = (('Ativo', 'Ativo'), ('Inativo', 'Inativo'))
    TIPO_CHOICES = (('Reserva', 'Reserva'), ('Saída', 'Saída'))
    data_locacao = models.DateField()
    data_devolucao = models.DateField()
    usuario =  CurrentUserField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    carro = models.ForeignKey('Automovel', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now=True)
    modificacado_em = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    valor_locacao = models.FloatField()
    valor_diaria = models.FloatField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Ativo')

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
        ('5', '5 Portas'), # Existe!
    )
    placa_automovel = models.CharField(max_length=15, unique=True,
                                       error_messages={'unique':"Já há um automóvel com esta placa!"})
    cor_automovel = models.CharField(max_length=20)
    nro_portas_automovel = models.CharField(max_length=10, choices=NRO_PORTAS_AUTOMOVEL_CHOICES)
    tipo_combustivel_automovel = models.CharField(max_length=50, choices=COMBUSTIVEL_CHOICES)
    quilometragem_automovel = models.FloatField()
    renavam_automovel = models.CharField(max_length=20, unique=True)
    valor_locacao = models.FloatField()
    motor = models.CharField(max_length=3)
    marca = models.CharField(choices=MARCA_CHOICES, max_length=50)
    modelo = models.CharField(max_length=200)
    ano = models.PositiveIntegerField()
    criado_em = models.DateTimeField(auto_now=True)
    categoria = models.CharField(choices=CATEGORIA_CHOICES, max_length=50)
    modificacado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Disponível')


    def __str__(self):
        carro = self.marca +' '+ self.modelo +' '+ str(self.ano) + ' - '
        carro += self.placa_automovel +' -- Diária padrão R$ '+ str(self.valor_locacao)
        return carro
