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
    path('visualizar_loc/<id>', views.visualizar_loc, name='visualizar_loc'),
    path('visualizar_cli/<id>', views.visualizar_cliente, name='visualizar_cli'),
    path('visualizar_vei/<id>', views.visualizar_veiculo, name='visualizar_vei'),
]
