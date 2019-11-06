from django.db import models


class Cliente(models.Model):
    STATUS_CHOICES = (('Ativo', 'a'), ('Inativo', 'i'))
    nome_cliente = models.CharField(max_length=100)
    cpf_cliente = models.CharField(max_length=50)
    rua_cliente = models.CharField(max_length=200)
    telefone_cliente = models.CharField(max_length=14)
    criado_em = models.DateTimeField(auto_now=True)
    email_cliente = models.CharField(max_length=20)
    modificacao_em = models.DateTimeField(auto_now_add=True)
    rg_cliente = models.CharField(max_length=50)
    cnpg_cliente = models.CharField(max_length=50)
    cnh_cliente = models.CharField(max_length=100)
    validade_cnh = models.CharField(max_length=50)
    numero_casa_cliente = models.IntegerField()
    bairro_cliente = models.CharField(max_length=50)
    cep_cliente = models.CharField(max_length=20)
    complemento = models.CharField(max_length=200)
    uf = models.CharField(max_length=10)
    cidade_cliente = models.ForeignKey('Cidade', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.nome_cliente


class Endereco(models.Model):
    rua = models.CharField('Rua', max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50)
    cep = models.CharField(max_length=30)
    bairro = models.CharField(max_length=20)
    cidade = models.ForeignKey('Cidade', max_length=25)

    def __str__(self):
        return self.rua

class Locacao(models.Model):
    STATUS_CHOICES = (('Ativo', 'a'), ('inativo', 'i'))
    dt_hora_locacao = models.CharField(max_length=50)
    dt_hora_devolucao = models.CharField(max_length=50)
    quilometragem = models.FloatField()
    valor_locacao = models.DecimalField(decimal_places=2)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    automovel = models.ForeignKey('Automovel', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now=True)
    modificacao_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.dt_hora_locacao


class Automovel(models.Model):
    STATUS_CHOICES = (('Ativo', 'a'), ('inativo', 'i'))
    placa_automovel = models.CharField(max_length=15)
    cor_automovel = models.CharField(max_length=10)
    nro_portas_automovel = models.IntegerField()
    tipo_combustivel_automovel = models.CharField(max_length=15)
    quilometragem_automovel = models.FloatField()
    chassi_automovel = models.IntegerField()
    valor_locacao = models.DecimalField(decimal_places=2)
    modelo_automovel = models.ForeignKey(on_delete=models.CASCADE)
    ano_automovel = models.IntegerField()
    marca_automovel = models.CharField(max_length=50)
    categoria_automovel = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now=True)
    modificacao_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)


    def __str__(self):
        return self.placa_automovel


class Marca(models.Model):
    descricao_marca = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao_marca


class Modelo(models.Model):
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return self.modelo


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=100)
    valor_diario = models.DecimalField(decimal_places=2)

    def __str__(self):
        return self.nome_categoria


        # Crie suas models aqui.
        # class Cliente(models.Model):
        #     pass