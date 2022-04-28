lista1 = ['Danton', 'José', 'Bertuol']
lista2 = ['Danton', 'José', 'Bertuol','Outros', 'Valores', 'Gerais']
n1, n2, n3 = lista1 # Desempacota os valores da lista nas 3 variáveis, dá erro caso seja um nr diferente de valores
n4, n5, *outros = lista2 # Desempacota e na última variável com o * atribui o restante dos valores criando nova lista
n6, n7, *outros, n8 = lista2 # Desempacota e pega o último valor da lista
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(outros)
print(n6)
print(n7)
print(n8)
print(outros)