from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat


def index(request):
    contatos = Contato.objects.order_by('-id').filter(mostrar=True) # Ordena em ordem descrescente pelo ID e filtra o que tem mostrar = True
    # Códigos para paginação
    paginator = Paginator(contatos, 20) # Mostra a quantidade "desejada" por página
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def ver_contato(request, contato_id):
    #contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })

def busca(request):
    termo = request.GET.get('termo') # Pega o valor do termo usando GET do request (formulário)

    if termo is None:
        raise Http404()

    campos = Concat('nome',Value(' '), 'sobrenome') # Concatena nome e sobrenome com espaço em branco no meio - Value simula

    contatos = Contato.objects.annotate(
        nome_completo=campos # Simula um campo com nome_completo
        ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo) # Filtra pelo nome completo ou pelo telefone. o Q faz o papel do "OU"
    )

    # Códigos para paginação
    paginator = Paginator(contatos, 20) # Mostra a quantidade "desejada" por página
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })
