'''
Formatando valores com modificadores
:s - Texto (strings)
:d - Inteiros (int)
:f - Float
:.(número)f - Quantidade de casas decimais (float)
:(caractere)(> ou < ou ^)(quantidade)(tipo - s, d ou f)
> - Esquerda
< - Direita
^ - Centro
'''

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

#Limitar para duas casas decimais com format e f-strings
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

#Inserir caracteres a esquerda, direita ou centro
#Esquerda
print(f'{num_1:0>10}')
#Direita
print(f'{num_1:0>10}')
#Centro
print(f'{num_1:0^10}')

#Formatado e com inserção de caracteres
print(f'{divisao:0^10.2f}')

#Utilizando formatacao com string
#Adiciona somente o excedente ao tamanho do valor
nome = 'Danton'
nome_formatado = '{n:@>7}'.format(n=nome)
print(f'{nome:*^10}')
print(nome_formatado)