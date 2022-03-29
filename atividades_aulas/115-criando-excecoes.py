# Definindo uma classe que herda de Exception você está criando uma exception
class TaErradoError(Exception):
    pass

def testaExc():
    raise TaErradoError('Errado!')

try:
    testaExc()
except TaErradoError as error:
    print(f'Erro {error}')
