class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod # Decora o método como um método de classe
    def por_ano_nascimento(cls, nome, ano): # cls significa a referência da classe
        idade = cls.ano_atual - ano # Calcula a idade com base no ano de nascimento
        return cls(nome, idade) # Executa a classe dentro do método

p1 = Pessoa('Danton', 25)
p2 = Pessoa('Mari', 29)
p3 = Pessoa.por_ano_nascimento('Jose', 1990)
print(p3.idade)
