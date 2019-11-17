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
    path('exluir_cliente/<id>', views.excluir_cliente, name='excluir_cliente'),
    path('excluir_loc/<id>', views.excluir_loc, name='excluir_loc'),
    path('excluir_automovel/<id>', views.excluir_automovel, name='excluir_veiculo'),
    path('excluir_cliente/<id>', views.excluir_cliente, name='excluir_cliente'),
    path('listar_auto_locados/', views.listar_auto_locados, name='listar_auto_locados'),
    path('fim_locacao/<id>', views.finalizar_loc, name='finalizar_loc'),
    path('accounts/', views.accounts, name='accounts'),
    path('register/', views.user_register, name='user_register'),
    path('senha/', views.change_password, name='change_password'),
    path('perfil/', views.perfil, name='perfil'),
    path('listar_usuarios/', views.listar_users, name='users'),
]
