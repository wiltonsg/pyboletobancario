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


if __name__ == '__main__':
    unittest.main()
