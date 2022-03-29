tupla1 = (1, 2, 3, 4, 5)
tupla2 = 1, 2, 4, 8, 16
tupla3 = tupla1 + tupla2 # Concatena tupças
tupla4 = ('Danton', 'Bertuol') * 3 # Repete 20x o valor da tupla
lista1 = list(tupla4) # Converte tupla em lista
tupla5 = tuple(lista1) # Converte lista em tupla
print(tupla1, type(tupla1))
print(tupla3)
print(tupla4)
print(lista1, type(lista1))

for v in tupla1: # Imprime todos os elementos linha a linha
    print(v)

print(tupla1[0:2]) # Fatiamento Tuplas