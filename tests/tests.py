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
        self.assertEqual(self.ticket._get_url(param1='value1'),
                         'https://www.boletobancario.com/boletofacil/integration/api/v1/param1=value1&')

    def test_get_url_two_params(self):
        self.assertEqual(self.ticket._get_url(param1='value1', param2='value2'),
                         'https://www.boletobancario.com/boletofacil/integration/api/v1/param1=value1&param2=value2&')

    def test_get_url_three_params(self):
        self.assertEqual(self.ticket._get_url(param1='value1', param2='value2', param3='value3'),
                         'https://www.boletobancario.com/boletofacil/integration/api/v1/param1=value1&param2=value2&param3=value3&')

    def test_get_url_param_none(self):
        self.assertEqual(self.ticket._get_url(param1='value1', param=None),
                         'https://www.boletobancario.com/boletofacil/integration/api/v1/param1=value1&')

    def test_get_url_params_none(self):
        self.assertEqual(self.ticket._get_url(param1='value1', param2='value2', param3=None),
                         'https://www.boletobancario.com/boletofacil/integration/api/v1/param1=value1&param2=value2&')


if __name__ == '__main__':
    unittest.main()
