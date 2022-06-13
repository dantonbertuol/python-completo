# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'João|Maria|ad....s', texto))
print(re.findall(r'João|joão|Maria', texto))
# [Jj] encontra se for maiúsculo ou minúsculo
print(re.findall(r'[Jj]oão|[Mm]aria', texto))
# [a-z] é qualquer letra entre a e z (usa o traço para intervalo)
print(re.findall(r'[a-z]aria', texto))
# [a-zA-Z0-9_.] é qualquer letra entre a-z minúsculo, A-Z maiúsculo e 0-9
print(re.findall(r'[a-zA-Z0-9_.]aria|[a-zA-Z0-9]oão', texto))
# a flag 're.I' [ignorecase] serve para não ser case sensitive
print(re.findall(r'jOãO|mAriA', texto, flags=re.I))
