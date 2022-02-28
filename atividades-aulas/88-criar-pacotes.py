import vendas.calc_precos
from vendas import calc_precos

preco = vendas.calc_precos.aumento(49.90, 15)
preco_2 = calc_precos.aumento(49.90, 15, formata=True)
print(preco, preco_2)
