'''
public: métodos e atributos que podem ser acessados dentro e fora da classe
protected: métodos e atributos que podem ser acessados dentro da classe ou das filhas
private: métodos e atributos que podem ser acessados apenas dentro da classe
_: underline no início de variável/método indica que é private (não torna private, mas 
existe uma convenção que mostra para os devs que é private)
__: dois underlines no início de variável/método o python utiliza uma função que renomeia o
atributo, então não tem como manipular ele fora da classe com o nome padrão, somente com
_NOMECLASSE__ATRIBUTO.
'''

class BaseDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados ['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados ['clientes'][id]

bd = BaseDados()
bd.inserir_cliente(1, 'Danton')
bd.inserir_cliente(2, 'Mari')
bd.inserir_cliente(3, 'Tania')
bd.apaga_cliente(2)
bd.lista_clientes()
