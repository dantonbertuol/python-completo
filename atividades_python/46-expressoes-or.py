nome = input('Qual o seu nome? ')

print(nome or None or False or 'Você não digitou nada.') # Se digitou algo (não está em branco)

a = 0
b = None
c = False
d = []
e = {}
f = 25
g = 'Danton'

variavel = a or b or c or d or e or f or g # Recebe o primeiro valor verdadeiro
print(variavel)
