from django import template

register = template.Library()

@register.filter(name='formata_comentarios') # Decora a função como um filtro
def formata_comentarios(num_comentarios):
    try:
        num_comentarios = int(num_comentarios)

        if num_comentarios == 0:
            return 'Nenhum comentário'
        elif num_comentarios == 1:
            return f'{num_comentarios} comentário'
        else:
            return f'{num_comentarios} comentários'
    except:
        return f'{num_comentarios} comentário(s)'
