
class MyException(Exception):
	pass

def propagarExcecao():
	raise MyException("Fui tapeado!")


try:
	propagarExcecao()
except Exception as exc:
	print(exc)