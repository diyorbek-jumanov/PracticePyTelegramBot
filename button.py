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


pprint(getupdates())
