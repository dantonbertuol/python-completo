'''
    Split - Dividr uma string
    Join - Juntar uma lista
    Enumerate - Enumerar elementos da lista
'''
##### Split #####
string1 = "O Brasil é o país do futebol, o Brasil é penta."
# Divide a string pelo espaço e cria uma lista de strings
lista1 = string1.split(' ')
print(lista1)
# Divide a string pela virgula e cria uma lista de strings
lista2 = string1.split(',')
print(lista2)

##### Join #####
# Join para unir em uma string um objeto iterável
string2 = "O Brasil é penta."
# Divide a string acima em uma lista
lista3 = string2.split(' ')
# Une a lista3 em uma nova variável, utilizando como separador a ','
string3 = ','.join(lista3)
print(string3)

##### Enumerate #####
# Enumerate desempacota a lista3 e atribui a v1 o indice e v2 o valor
for indice, valor in enumerate(lista3): 
    print(indice, valor)

lista4 = [[0, 'Danton'],[1, 'José'],[2, 'Bertuol']]
for indice, valor in lista4:
    print(indice, valor)
