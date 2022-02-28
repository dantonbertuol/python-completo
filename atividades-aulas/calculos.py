import math

PI = math.pi

def dobra_lista(lista):
    return [x * 2 for x in lista]

def multiplica_lista(lista):
    r = 1
    for i in lista:
        r *= i
    return r

# Dessa forma só vai executar se for executado especificamente este arquivo
# Caso ele seja importado por outro arquivo, como um módulo, essa parte não executa
if __name__ == '__main__':
    print(PI)
    print(dobra_lista([1,2,3,4,5]))
    print(multiplica_lista([1,2,3,4,5]))
    