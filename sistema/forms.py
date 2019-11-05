from django import forms
from .models import *


# # Exemplo
# # class ClienteForm(forms.ModelForm):
# #     class Meta:
# #         model = Cliente  # Model
# #         # Nome das variáveis em 'fields' deve ser o mesmo que em models.
# #         #fields = ('nome', 'email', 'telefone', 'rg', 'cpf', 'cnpj', 'rua',
# #                   'cnh', 'validade_cnh', 'rua', 'nro_casa', 'bairro', 'complemento',
# #                   'cep', 'uf', 'cidade', 'status')