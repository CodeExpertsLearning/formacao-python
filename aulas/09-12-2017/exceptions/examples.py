# while True:
#     try:
#         x = int(input("Por favor digite um numero: "))
#         break
#     except ValueError:
#         print("Oops!  Isto não é um número válido.  Tente novamente...")
#     except KeyboardInterrupt:
#     	print("\nVocê interrompeu a execução do programa!")
#     	break

# try:
# 	file = open('file.txt')
# 	s = file.readline()
# 	i = int(s.strip())
# 	file.close()
# except IOError:
# 	print("Arquivo não encontrado.")
# except ValueError:
# 	print("Arquivo vazio")

# try:
# 	import banco

# 	conta = banco.ContaBancaria("2367", "4567-x")
# # exceção gerada ao tentar abrir módulo/package que não existe
# except ImportError:
# 	print("Modulo banco não encontrado")