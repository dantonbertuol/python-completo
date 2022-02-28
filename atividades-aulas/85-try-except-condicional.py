def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    valor = converte_numero(input('Digite um número: '))
    if valor is None:
        print('Por favor digite um nḿero.')
    else:
        print(valor * 5)
