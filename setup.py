# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


DESCRIPTION = "Emita Boletos de Graça com CNPJ ou CPF. Você só é cobrado se receber!"

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass


setup(name='pyboletobancario',
      version='0.0.1',
      description='Emita Boletos de Graça com CNPJ ou CPF. Você só é cobrado se receber!',
      url='https://github.com/hudsonbrendon/pyboletobancario',
      author='Hudson Brendon',
      author_email='contato.hudsonbrendon@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['tests*']),
      install_requires=[
          'requests',
      ],
      zip_safe=False)
