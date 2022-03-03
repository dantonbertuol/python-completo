from time import time, sleep

def master(funcao):
    def slave(*args, **kwargs):
        print('Agora estou decorada')
        funcao(*args, **kwargs)
    return slave

# Função decorada com a master
@master
def fala_oi():
    print('Oi')

@master
def outra_funcao(msg):
    print(msg)

fala_oi()
outra_funcao('Olá')

# Verificar quanto demora para uma função ser executada #
def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao.__name__} levou {tempo:.2f}ms para executar.')
        return resultado
    return interna

@velocidade
def demora():
    for i in range(5):
        sleep(1)

demora()
