# Pyboletofacil

Emita Boletos de Graça com CNPJ ou CPF. Você só é cobrado se receber!

[![Build Status](https://travis-ci.org/hudsonbrendon/pyboletofacil.svg?branch=master)](https://travis-ci.org/hudsonbrendon/pyboletofacil)
[![Github Issues](http://img.shields.io/github/issues/hudsonbrendon/pyboletofacil.svg?style=flat)](https://github.com/hudsonbrendon/pyboletofacil/issues?sort=updated&state=open)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)

![Logo](logo.png)


# Instalação

```bash
$ pip install pyboletofacil
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
