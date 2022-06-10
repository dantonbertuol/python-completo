"""
TDD - Test Driven Development (Desenvolvimento guiado a testes)

Red (Ciclo do TDD)
Parte 1 - Criar o teste e ver falhar

Green (Ciclo do TDD)
Parte 2 - Criar o código e ver o teste passar

Refactor (Ciclo do TDD)
Parte 3 - Melhorar meu código
"""
# Esse try except serve para eu manipular o caminho onde irá buscar as classes (BaconComOvos por exemplo)
try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

import unittest
from baconcomovos import bacon_com_ovos

class TesteBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assertion_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos(1.5)

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida, msg=f'{entrada} não retornou "{saida}".')

    def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8)
        saida = 'Passar Fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida, msg=f'{entrada} não retornou "{saida}".')

    def test_bacon_com_ovos_deve_retornar_bacon_se_entrada_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12, 18, 21)
        saida = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida, msg=f'{entrada} não retornou "{saida}".')

    def test_bacon_com_ovos_deve_retornar_ovos_se_entrada_for_multiplo_de_5(self):
        entradas = (5, 10, 20, 25, 35)
        saida = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida, msg=f'{entrada} não retornou "{saida}".')

if __name__ == '__main__':
    unittest.main(verbosity=2)
