# -*- coding:utf-8 -*-

from .ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):

    def __init__(self, agencia:str, conta:str, cliente):
        super().__init__(agencia, conta)
        self__cliente = cliente