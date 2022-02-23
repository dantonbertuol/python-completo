'''
    Some o valor total do carrinho de compras utilizando list comprehensions
'''
carrinho = []
carrinho.append(('Produto 1', 50))
carrinho.append(('Produto 2', 40))
carrinho.append(('Produto 3', 30))
carrinho.append(('Produto 4', 20))
carrinho.append(('Produto 5', 10))
carrinho.append(('Produto 6', 60))
carrinho.append(('Produto 7', 70))
carrinho.append(('Produto 8', 80))

total = sum([float(valor) for prod, valor in carrinho])

print(total)