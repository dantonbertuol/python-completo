from dados import produtos, pessoas, lista

nova_lista = filter(lambda x: x > 5, lista) # Filtra apenas os números maiores que 5 e retorna uma nova lista
print(list(nova_lista))

novos_produtos = filter(lambda p: p['preco'] > 50, produtos) # Filtra produtos que tem preço maior que 50

for produto in novos_produtos:
    print(produto)

def filtra(produto):
    if produto['preco'] > 50:
        return True
    return False

novos_produtos = filter(filtra, produtos) # Filtra através de uma função e não lambda
for produto in novos_produtos:
    print(produto)