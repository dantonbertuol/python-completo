class A:
    vc = 123

a1 = A()
A.vc = 321 # Isso altera a variável de classe
a1.vc = 321 # Isso cria uma nova variável de instância