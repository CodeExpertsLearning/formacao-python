from .produto import Produto
from .desconto import Desconto

class Carrinho():

    def __init__(self):
        self.produtos = []
        self.valorTotal = 0

    def addProduto(self, produto: Produto):
        self.produtos.append(produto)
        self.valorTotal += produto.preco

    def aplicarDesconto(self, desconto: Desconto):
        desconto.calcularDesconto(self)