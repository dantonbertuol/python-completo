'''
    Operadores Lógicos
    and     e (retorna verdadeiro se todas forem verdadeiras)
    or      ou (retorna verdadeiro se ao menos uma for verdadeira)
    not     não (se verdadeiro é falso se falso é verdadeiro - inverte valor)
    in      está contido (verifica se o elemento está contido no conjunto)
    not in  não está contido (verifica se o elemento não está contido no conjunto)
'''

a = ''
b = 0
nome = 'Danton'

if not a and not b: # not serve para verificar itens em branco
    print('Por favor preencha a variável "a" e "b".')

if 'a' in nome:
    print(f"'a' pertence ao nome {nome}.")
else:
    print(f"'a' não pertence ao nome {nome}.")

user = input('Nome de usuário: ')
psw = input('Senha: ')
user_bd = 'danton'
psw_bd = '1234'

if user == user_bd and psw == psw_bd:
    print(f'Você está logado no sistema como {user_bd}')
else:
    print('Usuário não autenticado.')