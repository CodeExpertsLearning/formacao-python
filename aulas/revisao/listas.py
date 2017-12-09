
lista1 = [2,3.4, "python"]

# add objeto na lista
lista1.append((2,3,4))

# acessando o valor de uma lista
primeiro = lista1[0]

# pegar o indice de uma elemento
indice = lista1.index("python")

# remover elemento da lista
del lista1[0]

# pegar quantidade de elementos
len(lista1)

# Tuplas

tupla = (3,4,5)

# Operação indevida - Add elementos
try:
	tupla.append(3)
except Exception:
	print("Você não pode adicionar elementos na tupla")

# Operação indevida - Remover elemento
try:
	del tupla[0]
except Exception:
	print("Você não pode remover elementos da tupla")
