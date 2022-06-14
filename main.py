import requests
from colorama import Fore, init

init(convert=True)


def convert():

    url = 'https://passport.twitch.tv/login'

    username = input("Enter username: ")
    password = input("Enter password: ")
    
    json = {
        'username': username,
        'password': password,
        'client_id': '85lcqzxpb9bqu9z6ga1ol55du'
        }

    r = requests.post(url, json=json)

    if 'access_token' in r.text:
        token = r.json()['access_token']
        print(Fore.GREEN + token)
    t = open('tokens.txt', 'a')
    t.write(f'{token}\n')

convert()
