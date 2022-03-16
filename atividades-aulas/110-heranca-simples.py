'''
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
'''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print('Falando...')

class Cliente(Pessoa): # Passando a classe Pessoa por parâmetro quer dizer que o Cliente herda tudo de Pessoa
    def comprar(self): # Essa é exclusiva do cliente
        print('Comprando...')

class Aluno(Pessoa):  # Passando a classe Pessoa por parâmetro quer dizer que o Aluno herda tudo de Pessoa
    def estudar(self): # Essa é exclusiva do aluno
        print('Estudando...')

c1 = Cliente('Danton', 25)
print(c1.nome)
c1.falar()
c1.comprar()
a1 = Aluno('Mari', 29)
print(a1.nome)
a1.falar()
a1.estudar()
