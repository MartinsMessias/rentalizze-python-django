from django.urls import path
from . import views


urlpatterns = [
    path('', views.teste, name='teste'),
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente')
]