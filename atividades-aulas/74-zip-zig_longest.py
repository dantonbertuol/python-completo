from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Joaçaba', 'Belo Horizonte', 'Monte Belo']
estados = ['SP', 'SC', 'MG']

cidades_estados = zip(estados, cidades) # Une iteráveis (criou uma tupla com 2 índices) - Une até o índice da menor lista
                                        # 'Monte Belo' fica de fora
for valor in cidades_estados:
    print(valor)

# Une iteráveis (criou uma tupla com 2 índices) - Une até a maior lista E preenche com o valor padrão 'None'
# ou o informado no parametro fillvalue
cidades_estados = zip_longest(estados, cidades, fillvalue='Outro') 
for valor in cidades_estados:
    print(valor)