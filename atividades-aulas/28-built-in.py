'''
    Documentação e funções built-in úteis
'''

num_1 = input('Digite um número: ')
num_2 = input('Digite mais um número: ')

# Checa se a string tem só números e positivos com função
if(num_1.isdigit()) and (num_2.isdigit()):
    num_1 = int(num_1)
    num_2 = int(num_2)
    print(num_1 + num_2)
else:
    print('Não pude converter os números (função).')

# Com Try - Except
try:
    num_1 = float(num_1)
    num_2 = float(num_2)
    print(num_1 + num_2)
except:
    print('Não pude converter os números (try-except).')