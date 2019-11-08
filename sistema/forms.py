from django import forms
from .models import *


class ClienteForm(forms.ModelForm):
    nome_cliente = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf_cliente = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control cpf-inputmask', 'id': 'cpf_cliente', 'onkeyup': 'TestaCPF(this);'}), initial='00000000000')
    telefone_cliente = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control phone-inputmask'}))
    email_cliente = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email@email.com'}))
    rg_cliente = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}))
    cnpj_cliente = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control cnpj-inputmask', 'id': 'cnpj_cliente', 'onkeyup': 'validarCNPJ(this);'}), initial='0000000000000000')
    cnh_cliente = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    validade_cnh = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}))
    rua = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    numero = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    complemento = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cep = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    bairro = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    estado = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cidade = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cliente
        exclude = ('criado_em', 'modificado_em', )


class AutomovelForm(forms.ModelForm):

    class Meta:
        model = Automovel
        fields = '__all__'