from django import forms
from .models import *

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
    nome_cliente = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
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

    cnh_cliente = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    validade_cnh = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}))

    rua = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    numero = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'min': '0'}))

    complemento = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    cep = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    bairro = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    estado = forms.ChoiceField(choices=STATE_CHOICES, widget=forms.Select(attrs={'class': 'custom-select'}))

    cidade = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cliente
        exclude = ('criado_em', 'modificado_em',)


class AutomovelForm(forms.ModelForm):

    ano = forms.IntegerField(widget=forms.NumberInput(attrs={'min':1900}))
    class Meta:
        model = Automovel
        exclude = ('criado_em', 'modificado_em', )

    def __init__(self, *args, **kwargs):
        for l in self.base_fields:
            self.base_fields[l].widget.attrs['class'] = 'form-control'
        super(AutomovelForm, self).__init__(*args, **kwargs)