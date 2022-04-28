nome = 'Danton'
idade = 24
altura = 1.75
e_maior = idade > 18
peso = 72
imc = peso / (altura ** 2) # Calculo IMC

# Normal
print(nome, 'tem', idade, 'anos de idade e seu IMC é', round(imc,2))

# Formatação de string com 'f string' (não precisa preocupar com tipo de dado)
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}') #.2f significa duas casas decimais

# Formatação com 'format'
print('{} tem {} anos de idade e seu IMC é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu IMC é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu IMC é {im:.2f}'.format(n=nome, i=idade, im=imc))