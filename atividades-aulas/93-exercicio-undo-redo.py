'''
Faça uma lista de tarefas com as seguintes opções:
    Adicionar tarefa
    Listar tarefas
    Opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    Opção de refazer (a cada vez que chamarmos, refaz a última ação)
'''

def add_tarefa(lista, tarefa):
    lista.append(tarefa)
    return lista

def listar_tarefas(lista):
    if lista:
        print('Tarefas: ')
        for valor in lista:
            print(valor)
    else:
        print('Nenhuma tarefa para listar.')

def desfazer_tarefa(lista, lista_refazer):
    if lista:
        lista_refazer.append(lista.pop())
        return lista_refazer, lista
    else:
        print('Nenhuma tarefa para desfazer.')
        return lista_refazer, lista

def refazer_tarefa(lista, lista_refazer):
    if lista_refazer:
        lista.append(lista_refazer.pop())
        return lista_refazer, lista
    else:
        print('Nenhuma tarefa para refazer.')
        return lista_refazer, lista

lista_tarefas = []
lista_refazer = []
while True:
    print('1 - Adicionar Tarefa')
    print('2 - Listar Tarefas')
    print('3 - Desfazer Tarefa')
    print('4 - Refazer Tarefa')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        tarefa = input('Digite a tarefa: ')
        lista_tarefas = add_tarefa(lista_tarefas, tarefa)
    elif opcao == '2':
        listar_tarefas(lista_tarefas)
    elif opcao == '3':
        lista_refazer, lista_tarefas = desfazer_tarefa(lista_tarefas, lista_refazer)
    elif opcao == '4':
        lista_refazer, lista_tarefas = refazer_tarefa(lista_tarefas, lista_refazer)
    else:
        print('Opção inválida.')
