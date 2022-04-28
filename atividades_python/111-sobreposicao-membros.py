class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print('Falando...')

class Cliente(Pessoa): # Passando a classe Pessoa por parâmetro quer dizer que o Cliente herda tudo de Pessoa
    def comprar(self): # Essa é exclusiva do cliente
        print('Comprando...')

class ClienteVIP(Cliente):  # Passando a classe Cliente por parâmetro quer dizer que o ClienteVIP herda tudo de Cliente, que herdou tudo de Pessoa (é agregado)
    # Os métodos são buscados na ordem subclasse > superclasse
    def comprar(self): # Sobrepõe o método comprar do Cliente que herdou
        super().falar() # A palavra super() chama os métodos da superclasse, nesse caso o método falar da superclasse
        Cliente.falar(self) # Também pode ser chamado um método específico de uma classe
        print('Comprando na sala VIP...')

c1 = Cliente('Danton', 25)
c2 = ClienteVIP('Mari', 29)
c1.comprar()
c2.comprar()