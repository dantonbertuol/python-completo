def func(*args):  # Quantidade dinâmica de argumentos
    print(args)  # Os argumentos se tornam uma tupla
    print(args[0])  # Acessa o primeiro argumento
    print(args[-1])  # Acessa o último argumento
    print(len(args))  # Quantidade de argumentos
    list_args = list(args)  # Transforma o args de tupla para lista
    print(list_args)
    for v in args:  # Passar por todos os argumentos
        print(v)


func(1, 2, 3, 4, 5)
lista = [1, 2, 3, 4, 5]
func(*lista, 6, 7)  # Manda a lista desempacotada


def func_k(**kwargs):  # Key Word Argumentos, argumentos com palavra chave
    print(kwargs)
    print(kwargs['nome'])  # Se não existir vai dar erro
    print(kwargs.get('sobrenome'))  # Melhor forma de acessar o argumento


func_k(nome='Danton', sobrenome='Bertuol')
