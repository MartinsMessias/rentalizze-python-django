from django import forms
from .models import *
from datetime import date

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

    # Tipos e atributos dos campos que vai aparecer no template
    cpf_cliente = forms.CharField(
        required=False, # Que não vai ser obrigatório no template
        widget=forms.TextInput( # Definimos os atributos do campo, como ele vai aparecer no template
            attrs={'class': 'form-control cpf-inputmask', 'id': 'cpf_cliente', 'onkeyup': 'TestaCPF(this);'}
            # Lá(template) ele vai ser gerado assim:
            # <input class="form-control cpf-inputmask" type="text" id="cpf_cliente" onkeyup="TestaCPF(this);">
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

    # Incializa toda vez em que esse formulário for usado
    def __init__(self, *args, **kwargs):
        # Coloca em todos os campos que não tem uma 'class' do CSS, um 'form-control'.
        for l in self.base_fields:
            if not self.base_fields[l].widget.attrs.get('class'):
                self.base_fields[l].widget.attrs['class'] = 'form-control'

        super(ClienteForm, self).__init__(*args, **kwargs)

    # Valida CPF/CPNJ com valor 'None' direto do formulário
    # Sem isso eles não passariam no form.is_valid() na views.py
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
        # Define uma class CSS 'form-control' e o adiciona um js pra deixar as letras em maiúsculas.
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
               'onkeyup': 'calcular();'}))

    valor_diaria = forms.FloatField(
        required=False,
        widget=forms.NumberInput(
            attrs={'class': 'form-control decimal-inputmask',
               'onkeyup': 'calcular();'}))

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



# Formulário herdando tudo de LocacaoForm e alteramos somente o campo 'carro'
# pra aparecer todos os carros 'disponível' e 'indisponível' no formulário de edicão Locação
class EditLocacaoForm(LocacaoForm):
    carro = forms.ModelChoiceField(queryset=Automovel.objects.all())



class FimLocacaoForm(forms.Form):

    quilometragem = forms.FloatField(widget=forms.NumberInput())

    data_devolucao_f = forms.DateField(
        widget=forms.DateInput(attrs={'value': date.today(), 'type': 'date', 'class': 'form-control'}))

    valor_adicional = forms.FloatField(
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

