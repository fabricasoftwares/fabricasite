# Website da fábrica de software

O website da fábrica utiliza o framework [Django](https://www.djangoproject.com/), escrito em python, para gerenciar conteúdo.

## Virtualenv

O virtualenv do python isola as dependências de cada `ambiente` criado por ele, aconselha-se seu uso para esse projeto.

> Ver mais: [virtualenv](https://virtualenv.pypa.io/en/stable/)


## Para instalar as dependências do projeto

As dependências estão listadas no arquivo `requirements.txt`

```bash

pip install -r requirements.txt

```

## Para montar o banco de dados que será utilizado

```bash

cd /path/to/project

./manage.py migrate

```


## Para rodar a aplicação local

A aplicação, por default, fica disponível em `localhost:8000`

```bash

cd /path/to/project

./manage.py runserver

```

## Para rodar os testes

```bash

cd /path/to/project

./manage.py test

```

## Para acessar a documentação da API

> Acesse: http://localhost:8000/docs/
