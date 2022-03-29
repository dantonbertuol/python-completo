from dados import produtos, pessoas, lista
from functools import reduce

# Soma o total da lista
soma_lista = reduce(lambda ac, i: i + ac, lista, 0) # ac é o acumulador, i é o item, i + ac é a operação de todo loop.
print(soma_lista)

# Soma do preco dos produtos
soma_dic = reduce(lambda ac, p: p['preco'] + ac, produtos, 0) 
print(soma_dic)
