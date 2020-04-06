import cbpro


class CoinBasePro:

    public_client = cbpro.PublicClient()

    def __init__(self, config):
        self.auth_client = cbpro.AuthenticatedClient(
            config['API_KEY'], config['SECRET'], config['PASSPHRASE'])

    def amount_badge(self, id_badge):
        amount = self.auth_client.get_account(id_badge)
        return float(amount['balance'])

    def total_amount(self):
        amount_eth = self.amount_badge('c9b25431-6e04-4fc7-bd80-3f8d3e1ff060')
        amount_eur = self.amount_badge('ad260d00-a9bd-4dd6-995c-36b01ffb4efb')

        eth_price = self.eth_price()

        total = round(amount_eur + (amount_eth*eth_price), 2)

        return total

    def eth_price(self):
        return float(self.public_client.get_product_ticker(product_id='ETH-EUR')['price'])
