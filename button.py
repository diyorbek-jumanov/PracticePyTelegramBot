import os
import requests
from pprint import pprint

token = os.environ['token']

def getMe():
    url_getUpdates = f'https://api.telegram.org/bot{token}/getMe'
    respons_getMe = requests.get(url=url_getUpdates)
    
    return respons_getMe.json()


pprint(getMe())