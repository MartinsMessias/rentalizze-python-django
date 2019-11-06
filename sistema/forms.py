from django import forms
from .models import *


class ClienteForm(forms.ModelForm):
    nome_cliente = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf_cliente = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control cpf-inputmask', 'id':'cpf_cliente', 'onkeyup':'TestaCPF(this);'}))
    telefone_cliente = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control phone-inputmask'}))
    email_cliente = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'email@email.com'}))
    rg_cliente = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    cnpj_cliente = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control cnpj-inputmask', 'id':'cpf_cliente', 'onkeyup':'ValidarCNPJ(this);'}))
    cnh_cliente = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    validade_cnh = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))

    class Meta:
        model = Cliente
        fields = ('nome_cliente', 'cpf_cliente', 'telefone_cliente', 'email_cliente', 'rg_cliente', 'cnh_cliente', 'cnpj_cliente', 'validade_cnh')
