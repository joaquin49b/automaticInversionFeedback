import configparser
from coinbasepro import CoinBasePro

_CONFIG = configparser.ConfigParser()
_CONFIG.read('config.ini')

def main():

    coin_base_pro = CoinBasePro(_CONFIG['COINBASE_PRO'])

    coin_base_pro_amount = coin_base_pro.total_amount()
    print(coin_base_pro_amount)


if __name__ == '__main__':
    main()
    