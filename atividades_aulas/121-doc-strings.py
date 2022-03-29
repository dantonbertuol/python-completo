from typing import Union
# Documentação de uma linha
"""Documentação de uma linha"""

# Documentação com uma linha principal e outras várias linhas
"""Descrição rápida e simples.

Mussum Ipsum, cacilds vidis litro abertis.
Delegadis gente finis, bibendum egestas augue arcu ut est.
Tá deprimidis, eu conheço uma cachacis que pode alegrar sua vidis.
Interagi no mé, cursus quis, vehicula ac nisi.
In elementis mé pra quem é amistosis quis leo.
"""

# Documentação de função (primeira linha de uma função)
def soma(x, y):
    """Soma x e y"""
    return x+ + y

# Documentação de função (várias linhas)
def multiplica(x, y, z):
    """Multiplica x, y, z

    O programador pode omitir a variável z caso não tenha
    necessidade de usá-la.
    """

    return x * y * z

# Documentação de função com parametros
def multiplica2(x, y, z=None):
    """Multiplica x, y, z

    O programador pode omitir a variável z caso não tenha
    necessidade de usá-la.

    :param x: Primeiro Número
    :type x: int ou float
    :param y: Segundo Número
    :type y: int ou float
    :param z: Terceiro Número
    :type z: int, float ou None

    :return: A multiplicação entre x, y e z
    :rtype: int ou float
    """

    return x * y * z

# Documentação de classe vai na primeira linha também
class AA:
    """Documentação normal

    Vai virando longa
    Com quantas linhas quiser
    """
    pass

# Tipagem manual de variáveis
x: int = 10
y: float = 10.5
z: bool = False

# Função com especificação de tipo de dados de entrada e saida
           #entrada, #entrada, #entrada    #saida
def funcao(p1: float, p2: str, p3:dict) -> float:
    return 'a'

# Função com especificação de tipo de dados de entrada e mais de uma saida
           #entrada, #entrada, #entrada    # mais de uma saida
def funcao2(p1: float, p2: str, p3:dict) -> Union[str, float]:
    return 'a'

#print(x, y, z)

#multiplica2(1,2,3)
#print(multiplica2.__doc__)
#help(multiplica2)
#help(AA)
