from itertools import combinations, permutations, product

pessoa = ['Danton', 'Mari', 'Tania', 'Mauro', 'Dani', 'Laura']

for grupo in combinations(pessoa, 2): # Todas as combinações possiveis de pessoas em grupos de 2
    print(grupo) # Não tem ('Danton', 'Mari') e ('Mari', 'Danton') - apenas um deles

for grupo in permutations(pessoa, 2): # Todas as combinações possiveis de pessoas em grupos de 2
    print(grupo) # Tem ('Danton', 'Mari') e ('Mari', 'Danton') - ambos - Não tem valores repetidos ('Danton', 'Danton')

for grupo in product(pessoa, repeat=2): # Todas as combinações possiveis de pessoas em grupos de 2
    print(grupo) # Tem ('Danton', 'Mari') e ('Mari', 'Danton') - ambos - Tem valores repetidos ('Danton', 'Danton')