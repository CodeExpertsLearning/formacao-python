import zipfile

# try:
# 	arquivo = zipfile.ZipFile("banco.zip")
# 	arquivo.extractall(path="banco")
# 	arquivo.close()
# except OSError as ose:
# 	print("Algum problema ao ler o arquivo {}".format(ose.filename))

try:
	arquivo = zipfile.ZipFile('banco.zip')
except(FileNotFoundError, PermissionError):
	print("Algum problema ao ler o arquivo")
else:
	arquivo.extractall(path="banco")
	arquivo.close()