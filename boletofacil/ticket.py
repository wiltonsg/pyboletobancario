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

    # def issue_charge(self, description, payer_name, payer_cpf_cnpj,
    #                  reference=None, amount, due_date=None,
    #                  installments=None, max_overdue_days=None, fine=None,
    #                  interest=None, discount_amount=None, discount_days=None,
    #                  payer_email=None, payer_secondary_email=None, payer_phone=None,
    #                  payer_birth_date=None, billing_address_street=None,
    #                  billing_address_number=None, billing_address_complement=None,
    #                  billing_address_neighborhood=None, billing_address_city=None,
    #                  billing_address_state=None, billing_address_postcode=None,
    #                  notify_payer=None, notification_url=None, response_type='json',
    #                  fee_schema_token=None, split_recipient=None):
    #     data = requests.post(url)
