from zipfile import ZipFile
import os

# Para caminhos com barra invertida (\), utilize r
caminho = r'home/dantonbertuol/Desktop/arquivos'

# ESCREVE
with ZipFile('arquivos/arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)

# LISTA
with ZipFile('arquivos/arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# EXTRAI
with ZipFile('arquivos/arquivo.zip', 'r') as zip:
    zip.extractall('arquivos/descompactado')
