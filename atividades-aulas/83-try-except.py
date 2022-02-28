try:
    print(a)
except: # Pega qualquer tipo de erro (não é uma boa prática)
    print('Deu erro!')

try:
    print(a)
except NameError as erro: # Pega o erro "NameError" e atribui a variável erro
    print('Deu erro: ', erro) # Print no erro
except (IndexError, KeyError) as erro: # Pega mais de uma exceção nop mesmo except (exc1, exc2)
    print('Erro de índice.')
except Exception as erro: # Tratar outra exceção no mesmo try-except (Pega qualquer erro - Exception)
    print('Ocorreu um erro inesperado.')
else: # Else irá executar sempre que não ocorrer nenhuma "except" (exception)
    print('Deu Certo!')
finally: # Executa SEMPRE, se ocorrer ou não um erro
    print('Sempre executa')
    