from pessoa import Pessoa

p1 = Pessoa('Danton', 25) # Cria uma nova instância da classe passando as variáveis para o construtor (__init__)
p2 = Pessoa('Mari', 29) # Cria uma nova instância da classe passando as variáveis para o construtor (__init__)

p1.sobrenome = 'Bertuol' # Dessa forma um atributo é criado somente para a pessoa 1 (p1)
print(p1.sobrenome)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
