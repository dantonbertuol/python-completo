'''
Faça um programa que peça ao usuário para digitar um número inteiro.
Informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é.
'''

numero = input('Digite um número inteiro: ')

if numero.isnumeric():
    numero = int(numero)
    if numero % 2 == 0:
        print('É um número par.')
    else:
        print('É um número impar.')
else:
    print('O número informado não é inteiro.')


'''
Faça um programa que pergunte a hora ao usuário.
Baseando-se no horário exiba a saudação apropriada.
0-11: Bom dia. 12-17: Boa tarde. 18-23: Boa noite.
'''

hora = input('Digite a hora (0-23): ')

if hora.isnumeric():
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde.')
    elif hora >= 18 and hora <= 23:
        print('Boa noite.')
    else:
        print('A hora informada é inválida.')
else:
    print('A hora informada é inválida.')

'''
Faça um programa que peça o primeiro nome do usuário.
Se o nome tiver 4 letras ou menos informe "Seu nome é curto."
Se o nome tiver entre 5 e 6 letras informe "Seu nome é normal."
Se o nome tiver mais que 6 letras informe "Seu nome é muito grande."
'''

nome = input('Digite seu nome: ')
tam_nome = len(nome)

if tam_nome <= 4:
    print('Seu nome é curto.')
elif tam_nome >= 5 and tam_nome <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')