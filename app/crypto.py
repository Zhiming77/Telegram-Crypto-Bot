from requests import Session
import configparser
import json
import re
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

_symbols = ['btc', 'eth','usdt','ltc','uni','comp','nxm','atom','ren','mkr','yfi','aave','sushi','xrp','ada','zec','crv','snx','rune','sol','lrc','sc','grt','uma']

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['coinmarketcap']['api']

def get_crypto_price(api_key, symbols):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters ={
        'symbol': ','.join([_symbol.upper() for _symbol in _symbols])
    }

    headers = {
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)

        return (data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def render_crypto_results():

    api_key = get_api_key()
    data = get_crypto_price(api_key, _symbols)

    #creation of price dictionary via comprehension
    current_prices ={_symbol:"{0:.2f}".format(data['data'][_symbol.upper()]['quote']['USD']['price']) for _symbol in _symbols}

    #removal of characters that don't comply with Telegram MARKUP V2
    current_prices = {symbol: cleanPriceData(price) for symbol, price in current_prices.items()}

    return (current_prices)


def cleanPriceData(price):
    cleanr = re.compile(r'\.{1}')
    cleantext = re.sub(cleanr, r'\.', price)
    return cleantext




