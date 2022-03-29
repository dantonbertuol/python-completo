from os import sep


print('Danton', 'Bertuol') # Por padrão exibe um espaço entre os argumentos
print('Danton', 'Bertuol', sep='-') # Utiliza o traço como separador ao invés do espaço padrão
print('Danton', 'Bertuol', sep='-', end='##') # O argumento end indica com o que irá finalizar o print, por padrão é uma quebra de linha
print('Imprime na mesma linha do print acima separado por ##.')

# Exercício mascara cpf com print - 824.176.070-18
print('CPF: 824', '176', '070',sep='.',end='-')
print('18')
