'''
* Criar variáveis para nome (str), idade (int), altura(float) e peso (float)
* Criar variável com ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e ano atual)
* Obter o IMC da pessoa com 2 casas decimais (calcular)
* Exibir o texto com todos os valores na tela usando F-Strings
'''

nome = 'Danton'
idade = 24
altura = 1.75
peso = 72.0
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f"{nome} tem {idade} anos, {altura} de altura e pesa {peso} kgs.")
print(f"O IMC de {nome} é {imc:.2f}.")
print(f"{nome} nasceu em {ano_nascimento}")
