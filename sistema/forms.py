from django import forms
from .models import *
from datetime import date, time

class ClienteForm(forms.ModelForm):
    STATUS_CHOICES = (('Ativo', 'Ativo'), ('Inativo', 'Inativo'))
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
    cpf_cliente = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control cpf-inputmask', 'id': 'cpf_cliente', 'onkeyup': 'TestaCPF(this);'}
        )
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
        )
    )

    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'custom-select'}))
    rg_cliente = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}))
    validade_cnh = forms.CharField(widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control date-inputmask'}))
    numero = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'min': '0'}))
    estado = forms.ChoiceField(choices=STATE_CHOICES, widget=forms.Select(attrs={'class': 'custom-select'}))
    cep = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control cep-inputmask', 'min': '0'}))

    class Meta:
        model = Cliente
        exclude = ('criado_em', 'modificado_em',)

    def __init__(self, *args, **kwargs):
        for l in self.base_fields:
            if not self.base_fields[l].widget.attrs.get('class'):
                self.base_fields[l].widget.attrs['class'] = 'form-control'

        super(ClienteForm, self).__init__(*args, **kwargs)

    # Aceitar CPF/CPNJ com valor 'None'
    def clean_cpf_cliente(self):
        return self.cleaned_data['cpf_cliente'] or None

    def clean_cnpj_cliente(self):
        return self.cleaned_data['cnpj_cliente'] or None

class AutomovelForm(forms.ModelForm):
    ano = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1900}))
    motor = forms.FloatField(widget=forms.NumberInput(attrs={'min':'0.6','max':'6.8'}))
    class Meta:
        model = Automovel
        exclude = ('criado_em', 'modificado_em',)

    def __init__(self, *args, **kwargs):
        for l in self.base_fields:
            self.base_fields[l].widget.attrs['class'] = 'form-control'
            self.base_fields[l].widget.attrs['onkeyup'] = 'this.value=this.value.toUpperCase()'
        super(AutomovelForm, self).__init__(*args, **kwargs)


class LocacaoForm(forms.ModelForm):
    data_locacao = forms.CharField(
        widget=forms.TextInput(attrs={'value': date.today(), 'type': 'date', 'class': 'form-control date-inputmask'}))

    data_devolucao = forms.CharField(
        widget=forms.TextInput(attrs={'value': date.today(), 'type': 'date', 'class': 'date-inputmask form-control'}))

    valor_locacao = forms.FloatField(
        required=False,
        widget=forms.NumberInput(
            attrs={'readonly': 'true', 'class': 'btn-sm bg-success-light border-0', 'min': '0',
               'onkeyup': 'calcular();', 'onload': 'calcular();'}))

    valor_diaria = forms.FloatField(
        required=False,
        widget=forms.NumberInput(
            attrs={'class': 'form-control decimal-inputmask',
               'onkeyup': 'calcular();', 'onload': 'calcular();'}))

    cliente = forms.ModelChoiceField(queryset=Cliente.objects.filter(status='Ativo'))
    carro = forms.ModelChoiceField(queryset=Automovel.objects.filter(status='Disponível'))

    class Meta:
        model = Locacao
        exclude = ('criado_em', 'modificado_em', 'usuario', 'status',)

    def __init__(self, *args, **kwargs):
        for l in self.base_fields:
            if not self.base_fields[l].widget.attrs.get('class'):
                self.base_fields[l].widget.attrs['class'] = 'form-control'

        super(LocacaoForm, self).__init__(*args, **kwargs)


# Gamb pra aparecer todos os carros no formulário de edicão Locação
class EditLocacaoForm(LocacaoForm):
    carro = forms.ModelChoiceField(queryset=Automovel.objects.filter(status__icontains='disponível'))



class FimLocacaoForm(forms.Form):

    quilometragem = forms.FloatField(widget=forms.NumberInput())
    hora_devolucao = forms.TimeField(
        widget=forms.TimeInput(attrs={'value': time(), 'type': 'time', 'class': 'form-control'}))
    data_devolucao_f = forms.DateField(
        widget=forms.DateInput(attrs={'value': date.today(), 'type': 'date', 'class': 'form-control'}))
    valor_adicional = forms.CharField(
        required=False,
        widget=forms.NumberInput(
            attrs={'class': 'form-control','value':'0'}
        )
    )

    valor_locacao_f = forms.CharField(
        required=False,
        widget=forms.NumberInput(
            attrs={'class': 'form-control border-0 bg-success-light', 'readonly':'true'}
        )
    )

    def __init__(self, *args, **kwargs):
        for l in self.base_fields:
            if not self.base_fields[l].widget.attrs.get('class'):
                self.base_fields[l].widget.attrs['class'] = 'form-control'
        super(FimLocacaoForm, self).__init__(*args, **kwargs)

