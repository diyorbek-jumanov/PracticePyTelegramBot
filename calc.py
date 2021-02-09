import os
import requests
from pprint import pprint

token = os.environ['token']

# print(token)


def getupdates():
    url_getUpdates = f'https://api.telegram.org/bot{token}/getUpdates'
    respons_getUpdates = requests.get(url=url_getUpdates)

    return respons_getUpdates.json()['result'][-1]['message']


def sendKeyboard(idx, text):
    url_sendMessage = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': idx,
        'text': text,
        'reply_markup': {
            'keyboard': [
                [{'text': '7'}, {'text': '8'}, {'text': '9'}, {'text': '*'}],
                [{'text': '4'}, {'text': '5'}, {'text': '6'}, {'text': '/'}],
                [{'text': '1'}, {'text': '2'}, {'text': '3'}, {'text': '-'}],
                [{'text': '0'}, {'text': '.'}, {'text': '='}, {'text': '+'}]
            ],
            'resize_keyboard': True
        }

    }
    respons_sendKeyboard = requests.post(url=url_sendMessage, json=payload)

    pprint(respons_sendKeyboard.json())
    print(respons_sendKeyboard.url)

# pprint(getupdates())

msg_id = getupdates()['message_id']
# pprint(msg_id)

while True:
    data = getupdates()
    last_msg_id = data['message_id']
    print(last_msg_id)
    msg_text = data['text']
    # print(msg_text)
    chat_id = data['from']['id']
    # print(chat_id)
    if msg_id != last_msg_id:
        if msg_text == '/start':
            sendKeyboard(chat_id, 'calc')
            break
