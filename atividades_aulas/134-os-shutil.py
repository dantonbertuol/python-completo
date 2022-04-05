import os
import shutil

caminho_original = '/home/dantonbertuol/Documents/scripts'
caminho_novo = '/home/dantonbertuol/Documents/scripts2'

try:
    os. mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')
for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os. path.join(root, file)
        new_file_path = os. path.join(caminho_novo, file)
        # Move arquivo
        shutil.move(old_file_path, new_file_path)
        print(f'Arquivo {file} movido com sucesso!')
        # Copia arquivo
        shutil.copy(new_file_path, old_file_path)
        print(f'Arquivo {file} copiado com sucesso!')
        # Apaga arquivo
        os.remove(new_file_path)
        print(f'Arquivo {file} apagado com sucesso!')
