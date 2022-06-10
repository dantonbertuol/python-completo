# Esse try except serve para eu manipular o caminho onde irá buscar as classes (pessoa por exemplo)
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
from unittest.mock import patch
from pessoa import Pessoa

class TestPessoa(unittest.TestCase):

    # Função que sempre é executada antes de cada teste
    def setUp(self):
        self.p1 = Pessoa('Danton', 'Jose')

    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.nome, 'Danton')

    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.p1.nome, str)

    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Jose')

    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_ok(self):
        with patch('requests.get') as fake_request: # Cria dados fakes com Mock -> Patch
            fake_request.return_value.ok = True # Afirma que o retorno da requisição vai ter o 'ok' (dentre as coisas) como True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request: # Cria dados fakes com Mock -> Patch
            fake_request.return_value.ok = False # Afirma que o retorno da requisição vai ter o 'ok' (dentre as coisas) como False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_e_falha_sequencial(self):
        with patch('requests.get') as fake_request: # Cria dados fakes com Mock -> Patch
            fake_request.return_value.ok = True # Afirma que o retorno da requisição vai ter o 'ok' (dentre as coisas) como True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

            fake_request.return_value.ok = False # Afirma que o retorno da requisição vai ter o 'ok' (dentre as coisas) como True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)

if __name__ == '__main__':
    unittest.main(verbosity=2)
