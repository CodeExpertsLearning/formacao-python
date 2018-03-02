# Django Web Framework

O Django Framework é um framework Python de alto nível para aplicações web, que incentiva o desenvolvimento rápido e o design limpo e pragmático. É gratuito e de código aberto.

**Site Oficial**: https://www.djangoproject.com/

## Guia de Instalação

Como requisitos básicos para instalação, é necessário que você tenha instalado a ultima versão do Python 3, e também a ultima versão do Pip.

Para melhor aprendizagem, vou dividir a instalação por Sistema Operacional.

### Windows

Para instalar, abra o prompt de comando, e digite o seguinte comando:
```
pip install django
```
### Linux

Pra instalar o Django de forma global, utilize o seguinte comando:
```
$ python3 -m pip install --user django
```

Pra quem utiliza sistemas operacionais baseados em Linux, o ideal é que utilize um ambiente isolado de trabalho, utilizando o **Virtualenv**. Para instalar, utilize o seguinte comando:
```
$ python3 -m pip install --user virtualenv
```
Após instalar o virtualenv, crie o seu ambiente de trabalho na pasta desejada. Primeiramente, localize a pasta de instalação do Python 3, utilizando este comando:
```
$ which python3
```
Feito isso, crie seu ambiente isolado com o seguinte comando:
```
$ python3 -m virtualenv --python="(o caminho do python3)" myenv
```
Nesse caso, o "myenv" é o nome do virtualenv, e você pode alterar ao seu gosto. Este comando irá criar uma pasta com o nome do seu ambiente, que contém os arquivos de configuração do ambiente.

Para ativar o ambiente, utilize o seguinte comando:
```
$ source myenv/bin/activate
```

Com o seu ambiente ativado, instale o Django dentro dele, utilizando o seguinte comando:
```
$ pip install django
```
A partir daí, você já pode iniciar seu projeto, utilizando o seguinte comando:
```
$ django-admin startproject myproject
```

Para desativar o seu ambiente, utilize o seguinte comando:
```
$ deactivate
```
