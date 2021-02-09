import os
import requests
from pprint import pprint

token = os.environ['token']

# print(token)


def getupdates():
    url_getUpdates = f'https://api.telegram.org/bot{token}/getUpdates'
    respons_getUpdates = requests.get(url=url_getUpdates)

    return respons_getUpdates.json()['result'][-1]['message']


# pprint(getupdates())

msg_id = getupdates()['from']['id']
pprint(msg_id)
