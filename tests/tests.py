import unittest
import requests_mock

from boletofacil import Ticket


class TicketTestCase(unittest.TestCase):

    def setUp(self):
        self.ticket = Ticket()

    def test_creation_ticket(self):
        self.assertTrue(isinstance(self.ticket, Ticket))


if __name__ == '__main__':
    unittest.main()
