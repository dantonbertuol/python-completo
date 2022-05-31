from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from posts.models import Post

# Modelo Class Based Views - Com esse modelo pode herdar das classes
class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 1
    context_object_name = 'posts'

class PostBusca(PostIndex):
    ...

class PostCategoria(PostIndex):
    ...

class PostDetalhes(UpdateView):
    ...
