'''
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome
'''
def saudacao(saudacao, nome):
    print(saudacao, nome)
saudacao('Olá', 'Danton')

'''
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles
'''
def soma(num1, num2, num3):
    print(num1 + num2 + num3)

soma(10, 20, 30)

'''
3 - Crie uma função que receba 2 números. O primeiro é um valor e o
segundo um percentual. Retorne o valor do primeiro número somado
do aumento percentual do mesmo.
'''
def aumento(num, perc):
    return round(num * (1 + (perc/100)),2)

print(aumento(100, 10))

'''
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5 retorne buzz.
Se o parâmetro da função for divisível por 5 e 3 retorne FizzBuzz.
Caso contrário retorne o número enviado.
'''
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    if num % 5 == 0:
        return 'Buzz'
    if num % 3 == 0:
        return 'Fizz'
    return num

print(fizzbuzz(15))