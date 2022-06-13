# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1
# {n}
# {min, max}
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {5,10} De 5 a 10
# ()+ [a-zA-Z0-9]+

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem veem vem"!
Jã
'''
# '[o]+' significa que o conjunto de caracteres [o]
# pode se repetir quantas vezes quiser
# 'o+' significa que apenas o 'o' pode se repetir quantas vezes quiser
print(re.findall(r'j[o]+ão+', texto, flags=re.I))
# {1,} significa que o caracter a esquerda vai ser repetir
# ao menos 1 vez e no máximo ilimitado pois esta em branco
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))
# {3} significa que o caracter a esquerda se repete 3 vezes
# {1,2} significa que o caracter a esquerda se repete
# no mínimo 1 vez e no máximo 2
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))
# print(re.sub(r'jo{1,}ão{1,}', 'Felipe', texto, flags=re.I))

texto2 = 'João ama ser amado'
# quando aplica sobre um conjunto na expressao regular
# nao importa a ordem que os caracteres do conjunto aparecem no texto
print(re.findall(r'ama[od]{0,2}', texto2, flags=re.I))
