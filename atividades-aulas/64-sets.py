s1 = {1, 2, 3, 4, 5} # Cria um set
print(s1)
s2 = {1, 1, 2, 3, 4, 5} # Nos sets não pode ter elementos duplicados, neste caso será 1,2,3,4,5
print(s2)
s3 = set() # Outra forma de criar set
s3.add(1) # Adiciona elementos
s3.add(2) # Adiciona elementos
s3.add(3) # Adiciona elementos
print(s3)
s3.discard(2) # Remove elementos
print(s3)
s1.update('Python') # Adiciona cada elemento da string (letra) - ordem aleatória
print(s1)
s4 = s1 | s2 # Une sets

# Eliminar elementos duplicados de uma lista (elementos vao voltar fora de ordem)
l1 = [1,1,1,1,1,3,3,3,3,4,5,5,5,6,6,6,7,7,7,7,7,7,7]
print(l1)
l1 = set(l1)
l1 = list(l1)
print(l1)
