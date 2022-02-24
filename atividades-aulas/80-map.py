from dados import produtos, pessoas, lista

nova_lista = map(lambda x: x * 2, lista) # Para cada elemento da lista vai multiplicar por 2 e retorna uma nova lista
nova_lista2 = [x * 2 for x in lista] # Mesma função de cima com list comprehension
print(lista)
print(list(nova_lista))
print(nova_lista2)

def aumenta_preco(produto):
    produto['preco'] = produto['preco'] * 1.05
    return produto

produtos_novos = map(aumenta_preco, produtos) # Função map recebe uma função e um iteravel e aplica a função para todos os elementos

for produto in produtos_novos:
    print(produto)

nomes = map(lambda p: p['nome'], pessoas) # Retorna somente o nome das pessoas utilizando lambda

def aumenta_idade(pessoa):
    pessoa['nova_idade'] = round(pessoa['idade'] * 1.2)
    return pessoa

nova_pessoa = map(aumenta_idade, pessoas)

for pessoa in nova_pessoa:
    print(pessoa)
