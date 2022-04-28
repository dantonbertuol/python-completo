'''
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc.
'''

#Índices de uma string
#positivo  [012345678]
texto    = 'Python S2'
#negativo -[987654321]

#Imprime índice 2 da string
print("Primeiro caractere:", texto[2])

#Acessar o último caractere de uma string
print("Último caractere:", texto[-1])

#Slice - Fatiamento
nova_string = texto[2:6] #O 6 é exclusivo
print(nova_string)
nova_string2 = texto[:6] #Quando não tem o primeiro é do início (0)
print(nova_string2)
nova_string3 = texto[7:] #Quando não tem o último é até o final
print(nova_string3)

#Slice - Fatiamento (Negativo)
nova_string4 = texto[-9]
nova_string5 = texto[-9:-3]
nova_string6 = texto[:-1] #Exclui o último caracter
print(nova_string4)
print(nova_string5)
print(nova_string6)

#Slice - Fatiamento (step - passos)
nova_string7 = texto[0:6:2]
print(nova_string7)