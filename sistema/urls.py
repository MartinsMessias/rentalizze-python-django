from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('cadastrar_veiculo/', views.cadastrar_veiculo, name='cadastrar_veiculo'),
]