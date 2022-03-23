"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.
"""
from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._conta = None

    def inserir_conta(self, conta):
        self._conta = conta

    @property
    def conta(self):
        return self._conta

class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia} '
              f'Conta: {self.numero} '
              f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > self._saldo:
            print('Saldo insuficiente.')
            return
        self._saldo -= valor
        self.detalhes()

class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo, limite):
        super().__init__(agencia, numero, saldo)
        self._limite = limite

    def sacar(self, valor):
        if valor > self._saldo + self._limite:
            print('Saldo insuficiente.')
            return
        self._saldo -= valor
        self.detalhes()

class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False

        if cliente.conta not in self.contas:
            return False

        if cliente.conta.agencia not in self.agencias:
            return False

        return True

banco = Banco()

cliente1 = Cliente('Luiz', 30)
cliente2 = Cliente('Maria', 18)
cliente3 = Cliente('João', 50)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrente(2222, 254137, 0, 100)
conta3 = ContaPoupanca(1212, 254138, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(0)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado.')

print('####################')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado.')
