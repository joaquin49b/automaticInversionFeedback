import cbpro


class CoinBasePro:

    public_client = cbpro.PublicClient()

    def __init__(self, config):
        self.auth_client = cbpro.AuthenticatedClient(
            config['API_KEY'], config['SECRET'], config['PASSPHRASE'])

    def wallet(self, id_wallet):
        return self.auth_client.get_account(id_wallet)

    def eth_price(self):
        return self.public_client.get_product_ticker(product_id='ETH-EUR')['price']

    def total_amount(self):

        try:
            eth_wallet = self.wallet('c9b25431-6e04-4fc7-bd80-3f8d3e1ff060')
            eur_wallet = self.wallet('ad260d00-a9bd-4dd6-995c-36b01ffb4efb')

            eth_wallet = float(eth_wallet['balance'])
            eur_wallet = float(eur_wallet['balance'])

            eth_price = float(self.eth_price())

            total = round(eur_wallet + (eth_wallet*eth_price), 2)

            return total
        except KeyError as err:
            return err
        except ValueError as err:
            return err
