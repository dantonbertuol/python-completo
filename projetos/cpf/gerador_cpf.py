from random import randint

while True:
    cpf_validado = ''
    for valor in range(9):
        cpf_validado += str(randint(0,9))
    soma_dig_1 = 0
    soma_dig_2 = 0

    for indice, valor in enumerate(range(10,1,-1)):
        soma_dig_1 += int(cpf_validado[indice]) * valor

    digito_1 = 11 - (soma_dig_1 % 11)
    digito_1 = digito_1 if digito_1 <= 9 else 0

    cpf_validado += str(digito_1)

    for indice, valor in enumerate(range(11,1,-1)):
        soma_dig_2 += int(cpf_validado[indice]) * valor

    digito_2 = 11 - (soma_dig_2 % 11)
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_validado += str(digito_2)

    print(f'CPF Gerado {cpf_validado}')

    if input('Deseja gerar mais um CPF? (S ou N) ').upper() == 'N':
        break
    