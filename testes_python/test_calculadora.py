import unittest
from calculadora import soma

class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        # No primeiro parâmetro passa a função com os parâmetros
        # e no segundo o retorno esperado
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10,10,20),
            (5,5,10),
            (-10,-5,-15),
            (1.5,1.5,3),
            (100,100,200)
        )

        for x_y_saida in x_y_saidas:
            # Cria subtestes para cada teste
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        # Se levantar uma excecao de assertionerror passa no teste
        with self.assertRaises(AssertionError):
            soma('11', 11)

    def test_soma_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        # Se levantar uma excecao de assertionerror passa no teste
        with self.assertRaises(AssertionError):
            soma(11, '11')

unittest.main(verbosity=2)
