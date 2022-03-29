'''
Tipos de dados
str - string - Ex. 'Assim' ou "Assim"
int - inteiro - Ex. 10 20 30 40 50 -100 -200
float - real/ponto flutuante - Ex. 10.1 10.5 -10.4 -100.10
bool - booleano/lógico - Ex. True ou False
'''

# Type informa o tipo do dado
print('Danton', type('Danton'))
print(10, type(10))
print(100.5, type(100.5))
print(10 == 10, type(10 == 10))

# Casting de dados - converter o tipo
print(bool('Danton'))
print(float(10), type(float(10)))
print(int(100.8), type((100.8))) # Cuidado - exibe somente o número antes da virgula (inteiro)

# Exercicio - Exibir nome, idade, altura, se você é maior de idade
print('\n### Exercício - Exibir nome, idade, altura, se você é maior de idade ###')
print('Danton', type('Danton'))
print(24, type(24))
print(1.75, type(1.75))
print(24 > 18, type(24 > 18))
