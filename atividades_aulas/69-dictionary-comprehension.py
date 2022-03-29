lista = [
    ('chave', 2),
    ('chave2', 4)
]

d1 = {x: y*2 for x, y in lista}
print(d1)
d2 = {f'chave_{x}': x**2 for x in range(5)}
print(d2)