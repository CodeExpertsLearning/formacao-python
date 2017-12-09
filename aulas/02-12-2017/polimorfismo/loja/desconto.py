from abc import ABC, abstractmethod

class Desconto(ABC):

    @abstractmethod
    def calcularDesconto(self, carrinho):
        pass