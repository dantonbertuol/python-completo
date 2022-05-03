from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria') # Colunas que serão exibidas
    list_display_links = ('id', 'nome', 'sobrenome') # Colunas que terão link para acessar o contato
    #list_filter = ('nome', 'sobrenome') # Adiciona opções de filtragem
    list_per_page = 10 # Exibe 10 elementos por página
    search_fields = ('nome', 'sobrenome', 'telefone') # Insere campo de pesquisa por esses itens

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
