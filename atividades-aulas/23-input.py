nome = input("Qual o seu nome? ") # Função input retorna sempre uma string (str)
print(f'Usuário digitou {nome} e o tipo da variável é {type(nome)}.')

idade = int(input("Qual a sua idade? ")) # Converte para int o retorno da função input
print(f'A idade do {nome} é {idade} e o tipo da variável é {type(idade)}.')

ano_nascimento = 2022 - idade
print(f'{nome} nasceu em {ano_nascimento}.')

# Calculadora de soma
numero_1 = input("Digite um número: ")
numero_2 = input("Digite outro número: ")
print(numero_1 + numero_2) # Concatena
print(int(numero_1) + int(numero_2)) # Soma
