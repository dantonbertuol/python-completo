#indice   0,   1,   2,   3,   4,    5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
#indice - 6,   5,   4,   3,   2,    1

# Alterar valor de um índice da lista
lista[5] = 'F'

# Slice de listas (o 3 é exclusivo) - da mesma forma das strings
print(lista[0:3]) # Do início até o 3 (exclusivo)
print(lista[:3]) # Do início até o 3 (exclusivo)
print(lista[2:]) # Do 2 até o final
print(lista[0::2]) # Do início ao fim pulando 2 em 2
print(lista[::-1]) # Inverte a lista

# Funções com listas
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2 # Concatena listas
l1.extend(l2) # Concatena os valores (extendendo), mas a lista precisa existir
l1.extend('A') # Pode extender um único valor
l2.append('B') # Adiciona um elemento a lista (no final)
l2.insert(0,'C') # Insere um elemento no índice escolhido (0) e desloca os outros
l2.pop() # Remove o último elemento da lista
del(l2[3:5]) # Remove os elementos do slice informado
del(l2[1]) # Remove o elemento informado pelo índice
l2 = [1,2,3,4,5,6]
max(l2) # Retorna o maior valor da lista
min(l2) # Retorna o menor valor da lista

l4 = list(range(1, 10)) # Cria uma lista utilizando range (1 a 9)
print(l4)

for valor in l4:
    print(valor)

# Jogo com listas e laço de repetição
secreto = 'perfume'
digitadas = []
tentativas = 3
tentativa = 0

while True:
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    digitadas.append(letra)
    
    if letra in secreto:
        print(f'A letra "{letra}" existe na palavra secreta.')
    else:
        tentativa += 1
        print(f'A letra "{letra}" não existe na palavra secreta. Tentativa {tentativa} de {tentativas}.')
        digitadas.pop()
        
    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'
    if secreto_temp == secreto:
        print(f'Você ganhou! A palavra secreta era "{secreto}".')
        break
    else: 
        print(f'A palavra secreta está assim: "{secreto_temp}".')
    
    if tentativa == tentativas:
        print(f'Você perdeu! A palavra secreta era "{secreto}".')
        break
