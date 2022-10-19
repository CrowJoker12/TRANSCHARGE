from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cliente_id>', views.exibir_saldo, name='exibir_saldo'),
    path('<str:cliente_id>', views.erro500, name='erro'),
]
