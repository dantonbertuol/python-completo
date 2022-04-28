from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def falar(self, msg):
        pass

class B(A):
    def falar(self, msg):
        print(f'B está falando {msg}')

class C(A):
    def falar(self, msg):
        print(f'C está falando {msg}')

b = B()
c = C()
b.falar("Um Assunto")
c.falar("Outro Assunto")