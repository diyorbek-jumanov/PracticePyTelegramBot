import os
import requests
from pprint import pprint

token = os.environ['token']

def getMe():
    url_getMe = f'https://api.telegram.org/bot{token}/getMe'
    respons_getMe = requests.get(url=url_getMe)
    
    return respons_getMe.json()


# pprint(getMe())

def getupdates():
    url_getUpdates = f'https://api.telegram.org/bot{token}/getUpdates'
    respons_getUpdates = requests.get(url=url_getUpdates)

    return respons_getUpdates.json()


# pprint(getupdates())

def sendMessage(idx, text):
    url_sendMessage = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': idx,
        'text': text
    }
    respons_sendMessage = requests.get(url=url_sendMessage, params=payload)


def sendKeyboard(idx, text):
    url_sendMessage = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': idx,
        'text': text,
        'reply_markup': {
            'keyboard': [
                [{'text': 'button1'}]
            ],
            'resize_keyboard': True
        }

    }
    respons_sendKeyboard = requests.post(url=url_sendMessage, json=payload)

    pprint(respons_sendKeyboard.json())
    print(respons_sendKeyboard.url)


sendKeyboard(1258594598, 'salom')

