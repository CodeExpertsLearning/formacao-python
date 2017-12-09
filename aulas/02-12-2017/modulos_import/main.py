from banco import *

conta1 = ContaCorrente("2348", "4567-3", "Felipe")
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