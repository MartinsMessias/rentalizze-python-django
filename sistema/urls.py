from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('cadastrar_veiculo/', views.cadastrar_veiculo, name='cadastrar_veiculo'),
    path('cadastrar_locacao/', views.locar_veiculo, name='locar_veiculo'),
    path('listar_clientes/', views.listar_clientes, name='listar_clientes'),
    path('listar_veiculos/', views.listar_veiculos, name='listar_veiculos'),
    path('listar_locacoes/', views.listar_locacoes, name='listar_locacoes'),
    path('editar_locacao/<id>', views.editar_loc, name='editar_loc'),
    path('editar_cliente/<id>', views.editar_cliente, name='editar_cli'),
    path('editar_veiculo/<id>', views.editar_veiculo, name='editar_veiculo'),
    path('excluir_cliente/<id>', views.excluir_cliente, name='excluir_cliente')
]
