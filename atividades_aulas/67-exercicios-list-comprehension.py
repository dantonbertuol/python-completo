string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10 # Pula de 10 em 10 -> 0123456789
lista = [string[i:i + n] for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(lista)
print(retorno)
