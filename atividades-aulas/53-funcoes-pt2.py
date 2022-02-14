def funcao(var):
    return var

variavel = funcao('Valor que eu quero.')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')

def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2

resultado = divisao(10, 3)
if resultado:
    print(resultado)
else:
    print('Cálculo inválido.')

def retorna_funcao():
    return divisao # A função sem os parenteses é ela mesmo, ou seja, retorna a função

print(type(retorna_funcao))
print(retorna_funcao()(10,2))
func = retorna_funcao()
print(func(10, 5))

def retorna_tupla():
    return 'Danton', 'José' # Pode ser assim ou ('Danton','José')

print(retorna_tupla())