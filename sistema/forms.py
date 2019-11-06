from django import forms
from .models import *


class ClienteForm(forms.Form):
    class Meta:
        model = Cliente
        exclude = ('criado_em', 'modificado_em', )
