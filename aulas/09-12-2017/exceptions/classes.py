class MinhaException(Exception):
    pass


def gerar_excecao():
    raise MinhaException("Gerando uma exceção")

try:
    gerar_excecao()
except MinhaException as me:
    print(me)