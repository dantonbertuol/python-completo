import validadorcnpj.cnpj as util
from random import randint

while True:
    cnpj_gerado = ''
    for valor in range(8):
        cnpj_gerado += str(randint(0,8))
    cnpj_gerado += '0001'

    cnpj_gerado = util.dig_01(cnpj_gerado)
    cnpj_gerado = util.dig_02(cnpj_gerado)
    print(f'CNPJ Gerado {util.formata(cnpj_gerado)}')

    if input('Deseja gerar mais um CNPJ? (S ou N) ').upper() == 'N':
        break
