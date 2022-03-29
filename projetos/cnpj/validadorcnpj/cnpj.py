import re


# Remove os caracteres que não sejam números entre 0-9
def remove_caracter(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


# Formata o CNPJ
def formata(cnpj):
    return f'{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'


# Verifica se o CNPJ é uma sequência
def sequencia(cnpj):
    if cnpj[0] * len(cnpj) == cnpj:
        return True
    return False


# Calcula o módulo de 11
def mod_11(valor):
    return 11 - (valor % 11)


# Calcula o primeiro digito
def dig_01(cnpj):
    # Multiplicadores do primeiro digito
    multiplicadores = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    # List Comprehension para multiplicar listas
    escalar = sum([x * int(y) for x, y in (zip(multiplicadores, cnpj))])
    dig = mod_11(escalar)
    dig = dig if dig <= 9 else 0
    return cnpj + str(dig)


# Calcula o segundo digito
def dig_02(cnpj):
    # Multiplicadores do segundo digito
    multiplicadores = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    # List Comprehension para multiplicar listas
    escalar = sum([x * int(y) for x, y in (zip(multiplicadores, cnpj))])
    dig = mod_11(escalar)
    dig = dig if dig <= 9 else 0
    return cnpj + str(dig)

def valida(cnpj):
    cnpj_formatado = remove_caracter(cnpj)
    try:
        cnpj_validado = cnpj_formatado[0:12]
        cnpj_validado = dig_01(cnpj_validado)
        cnpj_validado = dig_02(cnpj_validado)
    except Exception:
        return False

    if cnpj_validado == cnpj_formatado and not sequencia(cnpj_formatado):
        return True
    return False
