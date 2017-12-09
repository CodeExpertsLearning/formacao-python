
class Objeto:

	def __init__(self, nome):
		self.nome = nome

class Duck:
	pass

def print_name(objeto):
	try:
		print(objeto.nome)
	except AttributeError:
		print("O objeto não possui o atributo 'nome' ")


obj = Objeto("Felipe")

pato = Duck()
# pato.nome = "Donald"

print_name(obj)
print_name(pato)