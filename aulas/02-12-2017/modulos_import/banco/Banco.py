# -*- coding: utf-8 -*-

from .ContaBancaria import ContaBancaria
class Banco:

    def __init__(self, nome):
        self.__nome = nome
        self.__contas = []

    def addConta(self, conta:ContaBancaria):
        self.__contas.append(conta)

    def setNome(self, nome:str):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def getContas(self):
        return self.__contas

    nome = property(fget=getNome, fset=setNome)