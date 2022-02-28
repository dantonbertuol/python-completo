from vendas.formata import preco

def aumento(valor, porcentagem, formata = False):
    if formata:
        return preco.real(valor + (valor * (porcentagem / 100)))
    return valor + (valor * (porcentagem / 100))
    
def reducao(valor, porcentagem, formata = False):
    if formata:
        return preco.real(valor - (valor * (porcentagem / 100)))
    return valor - (valor * (porcentagem / 100))