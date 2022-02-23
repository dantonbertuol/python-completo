nome = 'Danton'
iterador = iter(nome)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

# Quando exibe todos os indices do iterador ele é consumido por completo e não tem como recuperar os valores
# O mesmo serve para geradores e iteradores

# O for abaixo nao retorna nada
print('## FOR ##')
for v in iterador:
    print(v)
