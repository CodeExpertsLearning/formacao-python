from loja import *

prod1 = Produto("Notebook i7", 'Dell', 3200.00)
prod2 = Produto("Iphone X", 'Apple', 7200.00)
prod3 = Produto("Moto G5", 'Motorola', 900.00)

carrinho = Carrinho()
carrinho.addProduto(prod1)
carrinho.addProduto(prod2)

print("Valor total sem desconto: %.2f" % carrinho.valorTotal)
carrinho.aplicarDesconto(DescontoNatal())
print("Valor total depois do desconto: R$ %.2f" % carrinho.valorTotal)