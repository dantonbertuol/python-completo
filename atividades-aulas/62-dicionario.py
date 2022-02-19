import copy # Biblioteca para copiar dicionário

dicionario = {'chave':'valor'} # Criar Dicionário - Formato mais comum
dicionario['nova_chave'] = 'valor nova chave' # Adicionar novo chave-valor ao dicionário
dicionario['chave'] = 'valor atualizado' # Atualiza o valor - Mais utilizado
dicionario.update({'chave':'valor atualizado update'}) # Outra forma de atualizar o valor
print(dicionario['chave']) # Imprimir o valor de uma chave
dicionario2 = dict(chave1='Valor da chave', chave2='Valor da outra chave') # Outra forma de criar dicionário
print(dicionario2)
del dicionario['chave'] # Remove um valor do dicionário
print(dicionario)

dicionario3 = {'chave':'Danton','chave':'Bertuol'} # A chave deve ser única
print(dicionario3)

print(dicionario.get('nova_chave')) # Outra forma de acessar índice que não ocorre erro quando não existe
                                     # Se não existir retorna None, se existir retorna o valor

# Verificar se a chave contém no dicionário
if 'nova_chave' in dicionario:
    print(dicionario['nova_chave'])
else:
    print('Chave não existe')

print(dicionario.values()) # Acessa o valor do dicionário e não a chave
print(dicionario.keys()) # Acessa as chaves do dicionário e não a chave
print(len(dicionario)) # Quantidade de chave-valor no dicionário

# Iterar sobre dicionário (keys)
for k in dicionario2:
    print(k)

# Iterar sobre um dicionário (keys-value)
for k in dicionario2.items():
    print(k[0]) # chave
    print(k[1]) # valor

# Iterar com empacotamento
for k, v in dicionario2.items():
    print(k, v)

# Dicionário dentro de dicionário
clientes = {
    'cliente1': {
        'nome': 'Danton',
        'sobrenome': 'Bertuol'
    },
    'cliente2': {
        'nome': 'Mari',
        'sobrenome': 'Santini'
    }
}

# Iterando sobre clientes (dicionario dentro de dicionario)
for clientes_k, clientes_v in clientes.items():
    print(clientes_k)
    for cli_det_k, cli_det_v in clientes_v.items():
        print(cli_det_k, cli_det_v)

d1 = {1: 'a', 2: 'b', 3: 'c'}
v = d1 # Isso cria uma referência ao dicionário d1
v2 = d1.copy() # Isso cria uma cópia e perde a referência entre ambos (cópia rasa)
v3 = copy.deepcopy(d1) # Cria uma cópia profunda e ambos são totalmente independentes
v[1] = 'Danton' # Altera em ambos
v2[2] = 'Danton' # Altera somente em v2
print(d1)
print(v)
print(v2)

v3.pop(3) # Indica a chave a ser eliminada
v3.popitem() # Elimina o último item

v.update(v2) # Concatena dicionários
print(v)
