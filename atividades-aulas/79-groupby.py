from itertools import groupby, tee

alunos = [
    {'nome': 'Danton', 'nota': 'A'},
    {'nome': 'Mari', 'nota': 'B'},
    {'nome': 'Fabricio', 'nota': 'C'},
    {'nome': 'Mauro', 'nota': 'A'},
    {'nome': 'Tania', 'nota': 'B'},
    {'nome': 'Dani', 'nota': 'C'},
    {'nome': 'Tiago', 'nota': 'A'},
    {'nome': 'Laura', 'nota': 'B'},
    {'nome': 'Graci', 'nota': 'C'},
    {'nome': 'Jose', 'nota': 'A'},
]
ordena = lambda item: item['nota']
alunos.sort(key = ordena) # Ordenada pela nota com expressao lambda
print(alunos)
alunos_agrupados = groupby(alunos, ordena) # Agrupa pela nota. Porém precisa antes estar ordenado pelas notas para agrupar
print(alunos_agrupados)

for agrupamento, valores in alunos_agrupados:
    valores_len = tee(valores)
    print(f'Agrupamento: {agrupamento}')
    print(f'{len(list(valores_len))} alunos.') # Neste momento consome todos os itens do iterador
    for aluno in valores:
        print(f'\t{aluno}')