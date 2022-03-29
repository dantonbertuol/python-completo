'''
    Operadores Relacionais
    == igual
    >  maior
    >= maior ou igual
    <  menor
    <= menor ou igual
    != diferente
'''

num_1 = 10
num_2 = 10

# Atribui à expressão a comparação entre as duas variáveis
expressao = num_1 == num_2
print(expressao)

nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
idade_limite_min = 20
idade_limite_max = 30

if idade >= idade_limite_min and idade <= idade_limite_max:
    print(f'{nome} pode solicitar o empréstimo.')
else:
    print(f'{nome} não pode solicitar o empréstimo.')
