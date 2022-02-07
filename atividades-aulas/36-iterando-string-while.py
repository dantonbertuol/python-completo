frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
letra_maiscula = input('Qual letra deseja inserir como maiúcula? ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == letra_maiscula:
        nova_string += letra.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)
