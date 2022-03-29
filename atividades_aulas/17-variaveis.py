'''
Boas práticas para nomenclatura de variáveis: Iniciar com letra, pode conter números, separar _, letras minúsculas
'''

nome = 'Danton'
idade = 24
altura = 1.75
e_maior = idade > 18
peso = 72
imc = peso / (altura ** 2) # Calculo IMC

print(nome, 'tem', idade, 'anos de idade e seu IMC é', round(imc,2))
