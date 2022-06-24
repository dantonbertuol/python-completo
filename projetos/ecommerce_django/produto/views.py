from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from . import models


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 2


class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'


class AdicionarAoCarrinho(View):
    # Utiliza get pois o formulario eh get se nao seria post o metodo
    def get(self, *args, **kwargs):
        # Url de onde o cliente veio HTTP_REFERER
        http_referer = self.request.META.get(
            'HTTP_REFERER', reverse('produto:lista'))
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            messages.error(
                self.request,
                'Produto não existe'
            )
            # Direciona o cliente de onde ele veio com o metodo HTTP_REFERER
            return redirect(http_referer)

        variacao = get_object_or_404(models.Variacao, id=variacao_id)

        # Verifica se tem a chave carrinho na sessão
        if not self.request.session.get('carrinho'):
            # Se não existir cria com o nome carrinho (é um dicionario)
            self.request.session['carrinho'] = {}
            # Salva a sessão
            self.request.session.save()

        # Dicionario da sessao salvo na variavel carrinho
        carrinho = self.request.session['carrinho']

        # Se a variação já existe no carrinho
        if variacao_id in carrinho:
            # TODO: variação existe no carrinho
            pass
        else:
            # TODO: variação não existe no carrinho
            pass

        return HttpResponse(f'{variacao.produto} {variacao.nome} ')


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('RemoverDoCarrinho')


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
