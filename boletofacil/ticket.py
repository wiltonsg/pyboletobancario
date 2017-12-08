import operator
import requests


class Ticket(object):

    def __init__(self, token):
        self.__token = token
        self.__url = 'https://www.boletobancario.com/boletofacil/integration/api/v1/?token={}&'.format(self._token)

    @property
    def _token(self):
        return self.__token

    def _get_url(self, **kwargs):
        for param, value in sorted(kwargs.items(), key=operator.itemgetter(0)):
            if value:
                self.__url += '{}={}&'.format(param, value)
        return self.__url
