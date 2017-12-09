# -*- coding: utf-8 -*-

class ContaBancaria:

    """ Classe que abstrai o conceito de conta bancária """
    
    quant = 0

    def __init__(self, agencia, conta):
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = 0
        ContaBancaria.quant += 1

    def setAgencia(self, agencia):
        if ((type(agencia) == str) and (agencia != "")):
            self.__agencia = agencia

    def getAgencia(self):
        return self.__agencia

    def setConta(self, conta):
        if((type(conta) == str) and (conta != "")):
            self.__conta = conta

    def getConta(self):
        return self.__conta

    def deposito(self, value:float):
        if (value > 0):
            self.__saldo += value
            return True

    def saque(self, value:float):
        if (self.__saldo < value):
            raise Exception("Saldo insuficiente")
        
        self.__saldo -= value
        return True

    def getSaldo(self):
        return self.__saldo

    saldo = property(fget=getSaldo)
    agencia = property(fget=getAgencia, fset=setAgencia)
    conta = property(fget=getConta, fset=setConta)