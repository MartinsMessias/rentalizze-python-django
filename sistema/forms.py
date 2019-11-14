from django import forms
from .models import *
from datetime import date, time

STATE_CHOICES = (
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
    ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
    ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
)


class ClienteForm(forms.ModelForm):
    STATUS_CHOICES = (('Ativo', 'Ativo'), ('Inativo', 'Inativo'))
    cpf_cliente = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control cpf-inputmask', 'id': 'cpf_cliente', 'onkeyup': 'TestaCPF(this);'}
        ), initial='00000000000'
    )

    telefone_cliente = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control phone-inputmask'}
        )
    )

    email_cliente = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'email@email.com'}
        )
    )

    cnpj_cliente = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control cnpj-inputmask', 'id': 'cnpj_cliente', 'onkeyup': 'validarCNPJ(this);'}
        ), initial='0000000000000000'
    )

    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'custom-select'}))
    rg_cliente = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}))
    validade_cnh = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}))
    numero = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'min': '0'}))
    estado = forms.ChoiceField(choices=STATE_CHOICES, widget=forms.Select(attrs={'class': 'custom-select'}))

    class Meta:
        model = Cliente
        exclude = ('criado_em', 'modificado_em',)

    def __init__(self, *args, **kwargs):
        for l in self.base_fields:
            if not self.base_fields[l].widget.attrs.get('class'):
                self.base_fields[l].widget.attrs['class'] = 'form-control'

        super(ClienteForm, self).__init__(*args, **kwargs)


class AutomovelForm(forms.ModelForm):
    ano = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1900}))

    class Meta:
        model = Automovel
        exclude = ('criado_em', 'modificado_em',)

    def __init__(self, *args, **kwargs):
        for l in self.base_fields:
            self.base_fields[l].widget.attrs['class'] = 'form-control'
        super(AutomovelForm, self).__init__(*args, **kwargs)


class LocacaoForm(forms.ModelForm):
    data_locacao = forms.DateField(widget=forms.DateInput(attrs={'value': date.today(),'type': 'date', 'class': 'form-control'}))
    hora_locacao = forms.TimeField(widget=forms.TimeInput(attrs={'value': time(),'type': 'time', 'class': 'form-control'}))
    hora_devolucao = forms.TimeField(widget=forms.TimeInput(attrs={'value': time(), 'type': 'time', 'class': 'form-control'}))
    data_devolucao = forms.DateField(widget=forms.DateInput(attrs={'value': date.today(), 'type': 'date', 'class': 'form-control'}))

    class Meta:
        model = Locacao
        exclude = ('criado_em', 'modificado_em', 'usuario',)

    def __init__(self, *args, **kwargs):
        for l in self.base_fields:
            self.base_fields[l].widget.attrs['class'] = 'form-control'
        super(LocacaoForm, self).__init__(*args, **kwargs)
