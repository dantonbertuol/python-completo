from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

# Modelo Class Based Views - Com esse modelo pode herdar das classes
class PostIndex(ListView):
    ...

class PostBusca(PostIndex):
    ...

class PostCategoria(PostIndex):
    ...

class PostDetalhes(UpdateView):
    ...
