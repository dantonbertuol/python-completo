l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel for variavel in l1] # a cada iteração do laço for joga o valor na 'variavel'
l3 = [v * 2 for v in l1] # a cada iteração do laço for joga o valor na 'v' e multiplica por 2
l4 = [(v, v2) for v in l1 for v2 in range(3)] # Aninhamento de for e joga para uma tupla
l5 = ['Danton', 'Bertuol']
l6 = [v.replace('a', '@') for v in l5] # Replace de 'a' por '@' em cada elemento
print(l1, l2, l3, l4, l5, l6)

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)
l7 = [(y, x) for x, y in tupla] # Inverte os valores
print(l7)

l8 = list(range(100))
l9 = [v for v in l8 if v % 2 == 0] # Pega somente os números divisiveis por 2
l10 = [v for v in l8 if v % 3 == 0 if v % 8 == 0] # Pega somente os números divisiveis por 3 e por 8 (mais de um if)
l11 = [v if v % 3 == 0 else 'Não é' for v in l8] # Para usar o else
l12 = [v if v % 3 == 0 and v % 8 == 0 else 'Não é' for v in l8] # Para usar o if and e else
print(l9, l10, l11, l12)