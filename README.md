# Projeto Seazone

## Descrição do Projeto

O projeto Seazone é uma API RESTful criada com o Django Rest Framework. A API fornece funcionalidades para gerenciamento de reservas, com autenticação de usuários e criação, atualização e exclusão de reservas.

## Dependências

O projeto depende dos seguintes pacotes:

- Python 3.8 ou superior
- Django 4.2
- Django Rest Framework 3.14

## Instalação

1. Certifique-se de que você tem Python 3.8 ou superior instalado. Você pode baixar o Python a partir do [site oficial](https://www.python.org/downloads/).
2. Clone o repositório do projeto em sua máquina local: https://github.com/aramisSilva/seazone-test.git
3. Navegue até o diretório do projeto: `cd seazone-test`
4. Crie um ambiente virtual para o projeto: `python -m venv venv`
5. Ative o ambiente virtual: `source venv/bin/activate` se for windows: `venv\Scripts\activate`
6. Instale as dependências do projeto: `pip install -r requirements.txt`
7. Execute as migrações do banco de dados: `python manage.py migrate`
8. Crie um super usuário: `python manage.py createsuperuser`
9. Execute o servidor: `python manage.py runserver`
10. Acesse o servidor em http://localhost:8000
11. Acesse a documentação da API em http://localhost:8000/swagger
12. A API REST está disponível em `http://localhost:8000/api`

## Popular o banco de dados

1. python manage.py seed_reservas.py
2. python manage.py seed_anuncios.py
3. python manage.py seed_imoveis.py

## Testes
Você pode executar os testes do projeto com o seguinte comando:
python manage.py test

## Contribuição

Sinta-se à vontade para contribuir para o projeto. Faça um fork do projeto, crie uma nova branch, faça suas alterações e, em seguida, abra um pull request.

## Licença

Este projeto é licenciado sob a licença MIT.


