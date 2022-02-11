# Solução 1
print('Solução 01')
contador1 = 0
contador2 = 10
for valor in range(0,9):
    print(contador1, contador2)
    contador1 += 1
    contador2 -= 1

# Solução 2
print('Solução 02')
for indice, valor in enumerate(range(10, 1, -1)):
    print(indice, valor)
