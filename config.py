import configparser
import os
from decouple import config


auth = {}

auth['telegram_bot_token']=os.environ.get('BOT_TOKEN')
auth['channel']=os.environ.get('CHANNEL_ID')
auth['coinmarketcap_api']=os.environ.get('COINMARKETCAP_API')


if auth['telegram_bot_token'] == None:
    if config('telegram_bot_token')!="":
        auth['telegram_bot_token'] = config('telegram_bot_token')
    else:
        raise RuntimeError('telegram bot token not found 🙁! Put bot token🔐 in environmental variables!')
if auth['channel'] == None:
    if config('channel-id')!="":
        auth['channel'] = config('channel-id')
    else:
        raise RuntimeError('telegram channel not found 🙁! Put channel ID in environmental variables')
if auth['coinmarketcap_api']==None:
    if config('coinmarketcap-api')!="":
        auth['coinmarketcap_api'] = config('coinmarketcap-api')
    else:
        raise RuntimeError('coinmarketcap API not found 🙁! Put API in enviromental variables!')


config = configparser.ConfigParser()
config['coinmarketcap']={}
coinmarketcap_api = auth['coinmarketcap_api']
config['coinmarketcap']['api']= fr"{auth['coinmarketcap_api']}"
with open('config.ini', 'w') as configfile:
    config.write(configfile)
