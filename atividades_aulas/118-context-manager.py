from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()

with abrir('arquivos/abc.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')

'''
Gerenciador de contexto com classe
class Arquivo:
    def __init__(self, arquivo, modo):
        print('abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('retornando arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('fechando arquivo')
        self.arquivo.close()
        # Tratei a exceção
        return True

with Arquivo('arquivos/abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')
'''