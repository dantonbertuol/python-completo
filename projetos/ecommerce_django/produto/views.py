from email import message
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from . import models
from pprint import pprint


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
        # Se precisar destruir o carrinno e iniciar novamente
        # if self.request.session.get('carrinho'):
        #     del self.request.session['carrinho']
        #     self.request.session.save()

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
        variacao_estoque = variacao.estoque
        produto = variacao.produto

        produto_id = produto.id
        produto_nome = produto.nome
        variacao_nome = variacao.nome or ''
        preco_unitario = variacao.preco
        preco_unitario_promocional = variacao.preco_promocional
        quantidade = 1
        slug = produto.slug
        imagem = produto.imagem

        if imagem:
            imagem = imagem.name
        else:
            imagem = ''

        if variacao_estoque < 1:
            messages.error(self.request, 'Estoque insuficiente.')
            return redirect(http_referer)

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
            quantidade_carrinho = carrinho[variacao_id]['quantidade']
            quantidade_carrinho += 1

            if variacao_estoque < quantidade_carrinho:
                messages.warning(
                    self.request,
                    f'Estoque insuficiente para {quantidade_carrinho}x no '
                    f'produto {produto_nome}. Adicionamos {variacao_estoque}x '
                    f'no seu carrinho.'
                )
                quantidade_carrinho = variacao_estoque

            carrinho[variacao_id]['quantidade'] = quantidade_carrinho
            carrinho[variacao_id]['preco_quantitativo'] = preco_unitario * \
                quantidade_carrinho
            carrinho[variacao_id]['preco_quantitativo_promocional'] = preco_unitario_promocional * \
                quantidade_carrinho

        else:
            carrinho[variacao_id] = {
                'produto_id': produto_id,
                'produto_nome': produto_nome,
                'variacao_nome': variacao_nome,
                'variacao_id': variacao_id,
                'preco_unitario': preco_unitario,
                'preco_unitario_promocional': preco_unitario_promocional,
                'preco_quantitativo': preco_unitario,
                'preco_quantitativo_promocional': preco_unitario_promocional,
                'quantidade': quantidade,
                'slug': slug,
                'imagem': imagem
            }

        self.request.session.save()

        messages.success(
            self.request,
            f'Produto {produto_nome} {variacao_nome} adicionado ao seu '
            'carrinho.'
        )

        return redirect(http_referer)


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        # Url de onde o cliente veio HTTP_REFERER
        http_referer = self.request.META.get(
            'HTTP_REFERER', reverse('produto:lista'))
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            # Direciona o cliente de onde ele veio com o metodo HTTP_REFERER
            return redirect(http_referer)

        if not self.request.session.get('carrinho'):
            return redirect(http_referer)

        if variacao_id not in self.request.session['carrinho']:
            return redirect(http_referer)

        carrinho = self.request.session['carrinho'][variacao_id]

        messages.success(
            self.request,
            f'Produto {carrinho["produto_nome"]} {carrinho["variacao_nome"]} '
            f'removido do seu carrinho.'
        )

        del self.request.session['carrinho'][variacao_id]

        self.request.session.save()

        return redirect(http_referer)


class Carrinho(View):
    def get(self, *args, **kwargs):
        contexto = {
            'carrinho': self.request.session.get('carrinho', {})
        }
        return render(self.request, 'produto/carrinho.html', contexto)


class ResumoDaCompra(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
