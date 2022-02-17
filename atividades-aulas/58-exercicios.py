'''
1 - Crie uma função que recebe outra função como parâmetro e
retorne o valor da segunda função executada.
'''

def func1(func):
    return func('Olá Mundo')

def func2(valor):
    return (valor)

resultado = func1(func2)
print(resultado)

'''
2 - Crie uma função que recebe outra função como parâmetro e
retorne o valor da segunda função executada.
Faça a primeira função executar duas funções que recebam um número
diferente de argumentos.
'''

def mestre(fun, *args, **kwargs):
    return fun(*args, **kwargs)

def servo1(arg):
    return f'Oi {arg}'

def servo2(arg1, arg2):
    return f'{arg1} {arg2}'

resultado = mestre(servo1, 'Danton')
print(resultado)

resultado = mestre(servo2, 'Olá', 'Danton')
