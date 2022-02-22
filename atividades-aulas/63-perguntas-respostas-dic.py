perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '6',
            'd': '12'
        },
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 5 * 3?',
        'respostas': {
            'a': '15',
            'b': '4',
            'c': '13',
            'd': '21'
        },
        'resposta_certa': 'a'
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 2 * 8?',
        'respostas': {
            'a': '10',
            'b': '4',
            'c': '6',
            'd': '16'
        },
        'resposta_certa': 'd'
    },
}
print()
respostas_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk} - {pv["pergunta"]}')
    
    print('Escolha a opção correta:')

    for rk, rv in pv['respostas'].items():
        print(f'{rk} - {rv}')

    resposta_user = input('Digite sua resposta: ')

    if resposta_user == pv['resposta_certa']:
        print('Parabéns! Você acertou.')
        respostas_certas += 1
    else:
        print('Poxa, você errou!')
    print()

porcentagem_acerto = respostas_certas / len(perguntas)  * 100

print(f'Você acertou {respostas_certas} de {len(perguntas)}, um percentual de {porcentagem_acerto:.2f}%.')