fun_lambda = lambda x, y: x * y 
# É o equivalente a função:
# def mult(x, y):
#   return x * y

print(fun_lambda(2,2))

produtos = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

produtos.sort(key=lambda item: item[1])
print(produtos)
