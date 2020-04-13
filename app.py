# Version 1.0

import configparser
import os
from coinbase.wallet.error import APIError

from coinbasepro_api import CoinBasePro
from coinbase_api import CoinBase
from google_api import GoogleApi

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
SETTINGS_FILEPATH = os.path.join(SCRIPT_DIRECTORY, "config.ini")

_CONFIG = configparser.ConfigParser()
_CONFIG.read(SETTINGS_FILEPATH)


def main():
    try:
        coin_base_pro = CoinBasePro(_CONFIG['COINBASE_PRO'])
        coin_base = CoinBase(_CONFIG['COINBASE'])
        google_api = GoogleApi()

        coin_base_pro_amount = coin_base_pro.total_amount()
        coin_base_amount = coin_base.amount(
        ) + float(_CONFIG['COINBASE']['INVERSION'])

        google_api.save(
            coin_base_amount, _CONFIG['GOOGLE']['SHEET'], _CONFIG['COINBASE']['RANGE'])
        google_api.save(coin_base_pro_amount,
                        _CONFIG['GOOGLE']['SHEET'], _CONFIG['COINBASE_PRO']['RANGE'])

    except KeyError as err:
        print('Ha ocurrido un error, key no valida: ' + str(err))
    except ValueError as err:
        print('Ha ocurrido un error, número no valida: ' + str(err))
    except APIError as err:
        print('Ha ocurrido un error en la API de CoinBase: ' + str(err))


if __name__ == '__main__':
    main()
