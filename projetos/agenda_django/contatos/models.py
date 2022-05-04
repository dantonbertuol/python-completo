from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=255) # Campo tipo string com tamanho máximo 255

    # Será exibido no admin do django
    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=255) # Campo tipo string com tamanho máximo 255
    sobrenome = models.CharField(max_length=255, blank=True) # Campo tipo string com tamanho máximo 255, opcional (pode ser blank)
    telefone = models.CharField(max_length=255) # Campo tipo string com tamanho máximo 255
    email = models.CharField(max_length=255, blank=True) # Campo tipo string com tamanho máximo 255, opcional (pode ser blank)
    data_criacao = models.DateTimeField(default=timezone.now) # Campo tipo DateTime com o valor default
    descricao = models.TextField(blank=True) # Campo tipo Texto
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING) # FK para o Model Categoria
    mostrar = models.BooleanField(default=True) # Campo Booleano (T ou F)
    foto = models.ImageField(blank=True, upload_to=r'fotos/%Y/%m/%d') # Campo no formato imagem não obrigatório e o caminho

    def __str__(self):
        return self.nome
