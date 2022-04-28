variavel = ['Danton', 'AJosé', 'Bertuol']

for valor in variavel:
    if valor.lower().startswith('j'): # Convete para low (lowcase) e verifica se o valor começa com 'j'
        break
else:
    print('Não existe uma palavra que começa com "j".')
