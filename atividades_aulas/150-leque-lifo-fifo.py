# Pilha (stack) - LIFO - last in, first out.
livros = list()
livros.append ('Livro 1') # 1
livros.append ( 'Livro 2') # 2
livros.append ( 'Livro 3') # 3
livros.append ('Livro 4') # 4
livros.append ('Livro 5') # 5
livro_removido = livros.pop() # Remove 5
livro_removido = livros.pop() # Remove 4
livro_removido = livros.pop() # Remove 3
livro_removido = livros.pop() # Remove 2
livro_removido = livros.pop() # Remove 1
print(livros, livro_removido)

#Fila (queue) - FIFO - first in, first out.
from collections import deque
fila = deque()
fila.append('Joãozinho')
fila.append('Maria')
fila.append('Danton')
fila.append('Marcos')
fila.append('José')

print(f'Saiu: {fila.popleft()}') # Remove a esquerda da lista
print(f'Saiu: {fila.popleft()}') # Remove a esquerda da lista
print(f'Saiu: {fila.popleft()}') # Remove a esquerda da lista
print(f'Saiu: {fila.popleft()}') # Remove a esquerda da lista
print(f'Saiu: {fila.popleft()}') # Remove a esquerda da lista
for nome in fila:
    print(nome)

# Lista com número máximo de elementos
fila = deque(maxlen=10) # Define o número máximo de elementos da lista
for i in range(20):
    fila.append(i) # Quando passa o número máximo de elementos adiciona e remove o primeiro
    print(fila)

# Insere em um índice específico e joga os da direita um índice a mais
fila = deque(maxlen=10)
fila.extend([1, 2, 3, 4, 5, 6])
fila.insert(2, 'Danton José') # Inser no elemento 2
print(fila)

# Furar a fila com extendleft - Adiciona os elementos a esquerda
fila = deque(maxlen=10)
fila.extend([1, 2, 3])
fila.extendleft([4, 5, 6]) # Adiciona na esquerda para direita, do último elemento para o primeiro
print(fila)