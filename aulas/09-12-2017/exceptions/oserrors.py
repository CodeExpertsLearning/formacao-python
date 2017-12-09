from zipfile import ZipFile

# try:
# 	arquivo = ZipFile("banco.zip")
# 	arquivo.extractall(path="banco")
# 	arquivo.close()
# except Exception as ose:
# 	print("Algum problema ao ler o arquivo {}".format(ose.filename))

try:
	arquivo = ZipFile('files.zip')
	arquivo.extractall(path="files")
except FileNotFoundError:
	print("Arquivo não existe.")
except PermissionError:
	print("Sem permissão de leitura e/ou escrita")
else:	
	arquivo.close()