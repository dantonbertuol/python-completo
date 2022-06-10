def soma(x, y):
    """ Soma x e y
    Forma de escrever testes com doctest
    Na linha de cima chama a função e na linha de baixo o valor esperado do teste
    >>> soma(10, 20)
    30

    >>> soma(10, -10)
    0

    >>> soma(30, -20)
    10

    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float
    """
    assert isinstance(x, (int, float)), "x precisa ser int ou float"
    assert isinstance(y, (int, float)), "y precisa ser int ou float"
    return x + y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
