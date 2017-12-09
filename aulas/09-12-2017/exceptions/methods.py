
class MyException(Exception):
	pass

def propagarExcecao():
	raise MyException("Fui tapeado!")


try:
	propagarExcecao()
except MyException as exc:
	print(exc)