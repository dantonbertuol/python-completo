import sys # Importa o módulo sys inteiro
from sys import platform as plt # Importa somente o platform do módulo sys e define como apelido 'plt'
import random # Módulo random
from random import randint # Importa randint do rando, o problema é que teu código pode reescrever essa função

print(sys.platform) # Exibe a plataforma que ta sendo executada
print(plt) # Exibe a plataforma que ta sendo executada
print(random.randint(0, 10)) # Número aleatório entre 0 e 10 - Dessa forma não reescreve a função
print(randint(0, 10)) # Número aleatório entre 0 e 10