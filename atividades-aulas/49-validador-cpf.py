while True:
    cpf = input('Digite o CPF sem pontos (.) ou traçoes (-): ')
    cpf_validado = cpf[0:9]
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

    if cpf == cpf_validado:
        print(f'O CPF {cpf} é válido.')
    else:
        print(f'O CPF {cpf} é inválido.')
