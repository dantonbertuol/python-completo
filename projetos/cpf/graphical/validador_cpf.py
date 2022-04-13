import re

def valida_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf)
    if not cpf or len(cpf) != 11:
        return 'CPF Inválido'
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
        return 'CPF Válido'
    else:
        return 'CPF Inválido'
