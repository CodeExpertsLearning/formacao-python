import unittest
from conta import *

class ContaTest(unittest.TestCase):

    def setUp(self):
        self.conta = ContaBancaria('3456','2367-x')

    def test_create_conta(self):
        self.assertIsInstance(self.conta, ContaBancaria)

    def test_deposito(self):
        self.conta.deposito(200)
        self.assertEqual(200, self.conta.saldo)

    def test_saque(self):
        self.conta.deposito(500)
        self.conta.saque(300)
        self.assertEqual(200, self.conta.saldo)

    def test_saque_fails(self):
        self.conta.deposito(500)
        self.assertRaises(Exception, self.conta.saque, (600))

    def tearDown(self):
        print("Fim de teste")