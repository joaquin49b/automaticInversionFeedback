from coinbase.wallet.client import Client
from coinbase.wallet.error import APIError


class CoinBase:

    def __init__(self, config):
        self.auth_client = Client(config['API_KEY'], config['SECRET'])

    def amount(self):
        try:
            account = self.auth_client.get_account(
                "0ed05157-8cee-501a-bd7e-4fe2aa8d62b8")
            return float(account['native_balance']['amount'])
        except APIError as err:
            return err
