import sys
import time

lista = [0,1,2,3,4,5]

print(hasattr(lista,'__iter__')) # Verifica se é um iterável
print(hasattr(lista,'__next__')) # Verifica se é um iterador

lista = iter(lista) # Transforma a lista em um iterador
print(hasattr(lista,'__next__')) # Verifica se é um iterador
print(next(lista)) # indice 0
print(next(lista)) # indice 1
print(next(lista)) # indice 2

lista = list(range(100))
print(sys.getsizeof(lista)) # Quanto de memória consome a lista (bytes)

# Gerador 01 - Retorna um elemento por vez
def gera():
    for n in range(10):
        yield n
        time.sleep(0.1)

# Gerador 02
def gera2():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel

g = gera()
for v in g:
    print(v)

g2 = gera2()
print(next(g2))
print(next(g2))
print(next(g2))

lista = (x for x in range(100)) # Forma de declarar um gerador com list comprehension (muda os colchetes por parenteses)
print(type(lista))
print(sys.getsizeof(lista)) # Quanto de memória consome o gerador (bytes)