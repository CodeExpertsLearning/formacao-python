# -*- coding: utf-8 -*-

from .ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):

    def __init__(self, agencia:str, conta:str, cliente):
        super().__init__(agencia, conta)
        self__cliente = cliente

    def saque(self, valor:float):
        raise Exception("Você não pode efetuar saque")