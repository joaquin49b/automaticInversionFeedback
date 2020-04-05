import configparser
from base64 import b64encode
from coinbasepro import CoinBasePro

config = configparser.ConfigParser()
config.read('config.ini')

coin_base_pro = CoinBasePro(config['COINBASE_PRO'])

coin_base_pro_amount = coin_base_pro.total_amount()
print(coin_base_pro_amount)
