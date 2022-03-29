from itertools import count

# Gera um contador no formato iterador
contador = count() # Contador iterador infinito
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

for valor in contador:
    print(valor)
    if valor >= 10:
        break

contador = count(start=5, step=0.1) # Count com parâmetros

for valor in contador:
    print(valor)
    if valor >= 10:
        break

# Contadores com zip
contador = count()
nomes = ['Danton', 'Mari', 'Tania', 'Mauro']
lista = zip(contador, nomes)
print(list(lista))