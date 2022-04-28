def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log: ', error)
        raise # Relança a mesma exceção que recebeu

try:
    print(divide(2,0)) # Exceção zero division error
except ZeroDivisionError as error:
    print(error)

def divide2(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0.') # Lança uma exceção com o texto que você desejar
    else:
        return n1 / n2

try:
    print(divide2(2,0)) # Exceção zero division error
except ValueError as erro: # Captura o value error personalizado
    print(erro)
    