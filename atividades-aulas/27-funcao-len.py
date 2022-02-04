'''
    Função Len - para contar elemento
'''

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Usuário deve ter ao menos 6 caracteres.')
else:
    print('Você foi cadastrado.')

print(len(usuario))
print(usuario.__len__())
