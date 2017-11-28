
class ContaBancaria:

    quant = 0

    def __init__(self, agencia: str, conta: str):
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = 0
        ContaBancaria.quant += 1

    def setAgencia(self, agencia: str):
        if agencia:
            self.__agencia = agencia

    def getAgencia(self):
        return self.__agencia

    def setConta(self, conta: str):
        if conta:
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

class ContaCorrente(ContaBancaria):

    def __init__(self, agencia:str, conta:str, cliente):
        super().__init__(agencia, conta)
        self__cliente = cliente

class ContaPoupanca(ContaBancaria):

    def __init__(self, agencia:str, conta:str, cliente):
        super().__init__(agencia, conta)
        self__cliente = cliente

    def saque(self, valor:float):
        raise Exception("Você não pode efetuar saque")

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

conta1 = ContaCorrente("2348", "4567-3", "Pedro")
conta2 = ContaPoupanca("2389", "4567-8", "Joao")

conta1.deposito(500)
conta2.deposito(1000)

try:
    conta2.saque(20)
except Exception as e:
    print(e)

bradesco = Banco("Bradesco")
bradesco.addConta(conta1)
bradesco.addConta(conta2)

print(bradesco.nome)

print("Quantidade de Contas criadas:", ContaBancaria.quant)