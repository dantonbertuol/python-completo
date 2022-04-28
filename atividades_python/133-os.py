import os

caminho_procura = input('Digite o caminho: ')
termo_procura = input('Digite o termo a ser procurado: ')

def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        tamanho = tamanho 
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'

cont = 0
# Percorre todas as pastas/arquivos
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                cont += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
                tamanho_arquivo = os.path.getsize(caminho_completo)
                print()
                print('Encontrei o arquivo: ', arquivo)
                print('Caminho: ', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Extensão: ', extensao_arquivo)
                print('Tamanho: ', tamanho_arquivo)
                print('Tamanho formatado: ', formata_tamanho(tamanho_arquivo))
            except PermissionError as e:
                print('Sem Permissões.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            except Exception as e:
                print('Erro desconhecido: ', e)

print()
print(f'{cont} arquivo(s) encontrados.')
