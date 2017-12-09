import unittest
import requests_mock

from boletofacil import Ticket


class TicketTestCase(unittest.TestCase):

    def setUp(self):
        self.ticket = Ticket('12345')

    def test_creation_ticket(self):
        self.assertTrue(isinstance(self.ticket, Ticket))

    def test_token(self):
        self.assertEqual(self.ticket._token, '12345')

    def test_get_url(self):
        self.assertEqual(self.ticket._get_url(resource='issue-charge', param1='value1'),
                         'https://sandbox.boletobancario.com/boletofacil/integration/api/v1/issue-charge?'
                         'token=12345&param1=value1&')

    def test_get_url_two_params(self):
        self.assertEqual(self.ticket._get_url(resource='issue-charge', param1='value1', param2='value2'),
                         'https://sandbox.boletobancario.com/boletofacil/integration/api/v1/issue-charge?'
                         'token=12345&param1=value1&param2=value2&')

    def test_get_url_three_params(self):
        self.assertEqual(self.ticket._get_url(resource='issue-charge', param1='value1',
                                              param2='value2', param3='value3'),
                         'https://sandbox.boletobancario.com/boletofacil/integration/api/v1/issue-charge?'
                         'token=12345&param1=value1&param2=value2&param3=value3&')

    def test_get_url_param_none(self):
        self.assertEqual(self.ticket._get_url(resource='issue-charge', param1='value1', param=None),
                         'https://sandbox.boletobancario.com/boletofacil/integration/api/v1/issue-charge?'
                         'token=12345&param1=value1&')

    def test_get_url_params_none(self):
        self.assertEqual(self.ticket._get_url(resource='issue-charge', param1='value1', param2='value2', param3=None),
                         'https://sandbox.boletobancario.com/boletofacil/integration/api/v1/issue-charge?'
                         'token=12345&param1=value1&param2=value2&')

    @requests_mock.Mocker()
    def test_issue_charge(self, request_mock):
        url = 'https://sandbox.boletobancario.com/boletofacil/integration/api/v1/issue-charge?' \
              'token=12345&amount=500&description=pedido12345&payNumber=Testandoboleto&' \
              'payerCpfCnpj=10090997441&payerName=Hudson%20Brendon&'
        response = {'success': True,
                    'data': {'charges': [
                                         {'link': 'https://sandbox.boletobancario.com/',
                                          'code': 10069811, 'payNumber': 'BOLETO TESTE - Não é válido para pagamento',
                                          'checkoutUrl': 'https://sandbox.boletobancario.com/',
                                          'dueDate': '12/12/2017'}]}}
        request_mock.post(url, json=response)
        self.assertEqual(self.ticket.issue_charge(description='pedido12345',
                                                  amount=500, payerName='Hudson Brendon',
                                                  payerCpfCnpj=10090997441,
                                                  payNumber='Testandoboleto'), response)


if __name__ == '__main__':
    unittest.main()
