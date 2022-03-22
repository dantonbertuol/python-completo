# https://rszalski.github.io/magicmethods/

class AA:
    def __new__(cls, *args, **kwargs):
        print('Método new foi chamado')

        ## Limita a classe a uma declaração apenas por programa
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = super().__new__(cls)

        return cls._jaexiste

    # Faz a classe se comportar também como um função, podendo ser chamada diretamente
    def __call__(self, *args, **kwargs):
        return f'Argumentos enviados: {args} {kwargs}'

    def __len__(self):
        return 55

    def __init__(self, nome=None):
        print('INIT')

    def __str__(self):
        return 'O que quero exibir quando essa classe se transformar em uma str'

    def __del__(self):
        print('Objeto coletado.')

    # Toda vez que configurar um novo atributo na classe esse método é chamado
    def __setattr__(self, key, value):
        self.__dict__[key] = f'{value} adicionei isso no seu valor'


a = AA('Danton')
print(a)
