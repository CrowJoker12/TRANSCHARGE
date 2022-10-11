from django.shortcuts import render
from .models import Cliente


def index(request):
    clientes = Cliente.objects.all()
    return render(request, 'recarga/index.html',
                  {'clientes': clientes})


def exibir_saldo(request, cliente_id):
    cliente = Cliente.objects.get(cartao=cliente_id)
    return render(request, 'recarga/exibir_saldo.html',
                  {'cliente': cliente})


def handler404(request, exception):
    return render(request, 'recarga/404.html', status=404)


def handler500(request):
    return render(request, 'recarga/500.html', status=500)
