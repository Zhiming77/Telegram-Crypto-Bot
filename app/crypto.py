from requests import Session
import configparser
import json
import re
import sqlite3
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from apscheduler.schedulers.background import BackgroundScheduler
from bot_logic import threshold_reached

_symbols = ['btc', 'eth','usdt','uni','comp','nxm','atom','ren','mkr','yfi','aave','sushi','zec','crv','snx','rune','sol','lrc','sc','grt','uma']

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


check_id = 0.00

def threshold_check(check_id):
    current_prices = render_crypto_results()
    btc_price = current_prices['btc']
    conn = sqlite3.connect('alerts.db')
    c = conn.cursor()
    for row in c.execute('SELECT chat_id, price_threshold FROM alerts'):
        chat_id, price_threshold = row
        if btc_price >= price_threshold:
            remove_schedule(False, check_id=check_id)
            send_threshold_alert(btc_price)


def send_threshold_alert(price):
    price_alert_set = False
    remove_schedule(price_alert_set, check_id)
    threshold_reached()



def set_schedule(price_alert_set):
    if price_alert_set == True:
        scheduler = BackgroundScheduler()
        price_check =scheduler.add_job(threshold_check, 'interval', hours =1)
        check_id = price_check.id
        return check_id

def remove_schedule(price_alert_set, check_id):
    if price_alert_set == False:
        scheduler=BackgroundScheduler
        scheduler.remove_job(check_id)
