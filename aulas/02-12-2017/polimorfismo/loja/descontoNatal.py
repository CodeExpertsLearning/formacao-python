from .desconto import Desconto
from .carrinho import Carrinho

class DescontoNatal(Desconto):

    def calcularDesconto(self, carrinho: Carrinho):
        desconto = 0.20

        carrinho.valorTotal -= carrinho.valorTotal*desconto
