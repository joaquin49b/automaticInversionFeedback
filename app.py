import configparser
from coinbasepro_api import CoinBasePro
from coinbase_api import CoinBase

_CONFIG = configparser.ConfigParser()
_CONFIG.read('config.ini')


def main():

    coin_base_pro = CoinBasePro(_CONFIG['COINBASE_PRO'])
    coin_base = CoinBase(_CONFIG['COINBASE'])

    coin_base_pro_amount = coin_base_pro.total_amount()
    coin_base_amount = coin_base.amount()

    print('Coin base pro = ' + str(coin_base_pro_amount) +
          ' Coin Base = ' + str(coin_base_amount))


if __name__ == '__main__':
    main()
