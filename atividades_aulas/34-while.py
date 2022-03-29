# while True: # loop infinito
#     nome = input('Digite seu nome: ')
#     print(f'Olá {nome}!')

x = 0
while x < 10: # 0 a 9
    if x == 3:
        x = x + 1
        continue # essa palavra faz pular para o próximo laço (não executa o que está abaixo)
    if x == 8:
        break # essa palavra para a execução do loop
    print(x)
    x = x + 1

# Linhas e colunas
x = 0
y = 0

while x < 10:
    y = 0
    while y < 5:
        print(f'x vale {x} e y vale {y} ({x},{y}).')
        y += 1
    x += 1

# Calculadora
while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você deve digitar um número válido.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)
    if operador == '+':
        print(num_1+num_2)
    elif operador == '-':
        print(num_1-num_2)
    elif operador == '/':
        print(num_1/num_2)
    elif operador == '*':
        print(num_1*num_2)
    else: 
        print('Operador Inválido')
    
    sair = input('Deseja sair [s] ou [n]? ')
    if sair == 's':
        break
