# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1

import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>
'''
# Greedy
print(re.findall(r'<[dpiv]{1,3}>.+<\/[dpiv]{1,3}>', texto))
# Non-Greedy
print(re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', texto))
