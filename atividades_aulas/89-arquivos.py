# Formatos de abertura - https://docs.python.org/3/library/functions.html#open
import json
### Modo 01 de trabalhar com arquivos ###
print('Modo 01 de trabalhar com arquivos')
file = open('arquivos/arquivo.txt', 'w+') # Cria um arquivo com permissão de leitura/escrita
file.write('Linha 1\n') # Escreve linha 1
file.write('Linha 2\n') # Escreve linha 2
file.write('Linha 3\n') # Escreve linha 3

file.seek(0, 0) # Volta o cursor para o início do arquivo
print(file.read()) # Lê o arquivo inteiro

file.seek(0, 0) # Volta o cursor para o início do arquivo
print(file.readline(), end='') # Lê linha a linha 1
print(file.readline(), end='') # Lê linha a linha 2
print(file.readline(), end='') # Lê linha a linha 3

file.seek(0, 0) # Volta o cursor para o início do arquivo
print(file.readlines()) # Joga todas as linhas do arquivo para uma lista

file.seek(0, 0) # Volta o cursor para o início do arquivo
for linha in file.readlines(): # For percorre todas as linhas
    print(linha, end='')

file.close() # Fecha o arquivo

### Modo 02 de trabalhar com arquivos ###
print('Modo 02 de trabalhar com arquivos')
try:
    file = open('arquivos/arquivo.txt', 'w+') # Cria um arquivo com permissão de leitura/escrita
    file.write('Linha 1\n') # Escreve linha 1
    file.seek(0, 0) # Volta o cursor para o início do arquivo
    print(file.read())
finally: # No Finally pra garantir que vai executar
    file.close() # Fecha o arquivo

### Modo 03 de trabalhar com arquivos (pyhonico) - Gerenciador de contexto ###
print('Modo 03 de trabalhar com arquivos (pyhonico) - Gerenciador de contexto')
# Com o with abre e fecha o arquivo no final de executar
with open('arquivos/arquivo.txt', 'w+') as file:
    file.write('Linha 1\n') # Escreve linha 1
    file.write('Linha 2\n') # Escreve linha 2
    file.write('Linha 3\n') # Escreve linha 3

    file.seek(0, 0)
    print(file.read())

### Trabalhando com arquivos json e dicionários ###
d1 = {
    'Pessoa 1': {
        'nome': 'Danton',
        'idade': 24
    },
    'Pessoa 2': {
        'nome': 'Mari',
        'idade': 28
    }
}
d1_json = json.dumps(d1) # Converte o dicionário para json
with open('arquivos/arquivo.json', 'w+') as file: # Cria o arquivo json
    file.write(d1_json) # Escreve o dicionário em json

with open('arquivos/arquivo.json', 'r') as file: # Abre o arquivo json como leitura
    d1_json = file.read() # Lê as linhas
    d1 = json.loads(d1_json) # Converte de volta para dicionário

print(d1)
