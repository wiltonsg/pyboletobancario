# Pyboletobancario

Emita Boletos de Graça com CNPJ ou CPF. Você só é cobrado se receber!

[![Build Status](https://travis-ci.org/hudsonbrendon/pyboletobancario.svg?branch=master)](https://travis-ci.org/hudsonbrendon/pyboletobancario)
[![Github Issues](http://img.shields.io/github/issues/hudsonbrendon/pyboletobancario.svg?style=flat)](https://github.com/hudsonbrendon/pyboletobancario/issues?sort=updated&state=open)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)

![Logo](logo.png)


# Instalação

```bash
$ pip install pyboletobancario
```
ou

```bash
$ python setup.py install
```

# Modo de uso

## Geração de cobrança

```python
>>> from ticket import Ticket

>>> ticket = Ticket(<TOKEN>)

>>> ticket.issue_charge(description='your description', amount=100, payerName='Hudson Brendon', payerCpfCnpj=10090997452)
```
Para a lista completa de argumentos visite a documentação da API em: https://www.boletobancario.com/boletofacil/integration/integration.html#cobrancas

# Listar cobranças

```python
>>> from ticket import Ticket

>>> ticket = Ticket(<TOKEN>)

>>> ticket.list_charges(beginDueDate='dd/mm/yyyy', endDueDate='dd/mm/yyy')
```

Ou

```python
>>> from ticket import Ticket

>>> ticket = Ticket(<TOKEN>)

>>> ticket.list_charges(beginPaymentDate='dd/mm/yyyy', endPaymentDate='dd/mm/yyy')
```
Para a lista completa de argumentos visite a documentação da API em: https://www.boletobancario.com/boletofacil/integration/integration.html#list_charges

# Consulta de saldo

```python
>>> from ticket import Ticket

>>> ticket = Ticket(<TOKEN>)

>>> ticket.fetch_balance()
```
Para a lista completa de argumentos visite a documentação da API em: https://www.boletobancario.com/boletofacil/integration/integration.html#saldo


# Solicitação de transferência

```python
>>> from ticket import Ticket

>>> ticket = Ticket(<TOKEN>)

>>> ticket.request_transfer(amount=100.00)
```
Para a lista completa de argumentos visite a documentação da API em: https://www.boletobancario.com/boletofacil/integration/integration.html#transferencia

# Cancelamento de cobrança

```python
>>> from ticket import Ticket

>>> ticket = Ticket(<TOKEN>)

>>> ticket.cancel_charge(code=12345)
```
Para a lista completa de argumentos visite a documentação da API em: https://www.boletobancario.com/boletofacil/integration/integration.html#cancel_charge

# Como contribuir?

Clone o projeto no seu PC:

```bash
$ git clone https://github.com/hudsonbrendon/pyboletobancario.git
```

Certifique-se de que o [Pipenv](https://github.com/kennethreitz/pipenv) está instalado, caso contrário:

```bash
$ pip install -U pipenv
```

No diretório pyboletobancario instale as dependências executando o comando abaixo:

```bash
$ pipenv install --dev
```

# Licença

[MIT](http://en.wikipedia.org/wiki/MIT_License)
