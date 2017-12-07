import requests


class Ticket(object):

    def __init__(self, token):
        self.__url = 'https://www.boletobancario.com/boletofacil/integration/api/v1/'
        self.__token = token

    @property
    def _token(self):
        return self.__token
