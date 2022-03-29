# Quando importa um módulo ele executa tudo que ta dentro dele (prints, calculos, etc) - Exceto se estiver no if do __main__
import calculos # Importa o fonte calculos (como se fosse um módulo/biblioteca personalizado)

print(calculos.PI)
print(calculos.dobra_lista([1,2,3,4,5]))
print(calculos.multiplica_lista([1,2,3,4,5]))
