from requests import Session
import configparser
import json
import re
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['coinmarketcap']['api']

def get_crypto_price(api_key):

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters ={
        'symbol':'BTC,ETH,USDT,XRP,LTC,ADA,UNI,COMP,NXM,ATOM,REN,MKR,YFI,AAVE,SUSHI'
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
    data = get_crypto_price(api_key)

    current_prices ={}

    current_prices['btc'] = "{0:.2f}".format(data['data']['BTC']['quote']['USD']['price'])
    current_prices['eth'] = "{0:.2f}".format(data['data']['ETH']['quote']['USD']['price'])
    current_prices['usdt'] = "{0:.2f}".format(data['data']['USDT']['quote']['USD']['price'])
    current_prices['ltc'] = "{0:.2f}".format(data['data']['LTC']['quote']['USD']['price'])
    current_prices['uni'] = "{0:.2f}".format(data['data']['UNI']['quote']['USD']['price'])
    current_prices['comp'] = "{0:.2f}".format(data['data']['COMP']['quote']['USD']['price'])
    current_prices['nxm'] = "{0:.2f}".format(data['data']['NXM']['quote']['USD']['price'])
    current_prices['atom'] = "{0:.2f}".format(data['data']['ATOM']['quote']['USD']['price'])
    current_prices['ren'] = "{0:.2f}".format(data['data']['REN']['quote']['USD']['price'])
    current_prices['mkr'] = "{0:.2f}".format(data['data']['MKR']['quote']['USD']['price'])
    current_prices['yfi'] = "{0:.2f}".format(data['data']['YFI']['quote']['USD']['price'])
    current_prices['aave'] = "{0:.2f}".format(data['data']['AAVE']['quote']['USD']['price'])
    current_prices['sushi'] = "{0:.2f}".format(data['data']['SUSHI']['quote']['USD']['price'])
    current_prices['xrp'] = "{0:.2f}".format(data['data']['XRP']['quote']['USD']['price'])
    current_prices['ada'] = "{0:.2f}".format(data['data']['ADA']['quote']['USD']['price'])


    current_prices = {symbol: cleanPriceData(price) for symbol, price in current_prices.items()}

    return (current_prices)


def cleanPriceData(price):
    cleanr = re.compile(r'\.{1}')
    cleantext = re.sub(cleanr, r'\.', price)
    return cleantext



