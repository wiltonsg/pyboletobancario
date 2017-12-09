import operator
import requests


class Ticket(object):

    def __init__(self, token):
        self.__token = token
        self.__url = 'https://sandbox.boletobancario.com/boletofacil/integration/api/v1/{}?token={}&'

    @property
    def _token(self):
        return self.__token

    def _get_url(self, resource, **kwargs):
        url = self.__url.format(resource, self._token)
        for param, value in sorted(kwargs.items(), key=operator.itemgetter(0)):
            if value:
                url += '{}={}&'.format(param, value)
        return url

    def issue_charge(self, description, amount, payerName, payerCpfCnpj, **kwargs):
        try:
            data = requests.post(self._get_url(resource='issue-charge',
                                               description=description,
                                               amount=amount,
                                               payerName=payerName,
                                               payerCpfCnpj=payerCpfCnpj,
                                               **kwargs)).json()
        except Exception as error:
            raise error
        return data
