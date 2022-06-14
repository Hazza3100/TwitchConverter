import requests

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
        print(token)

convert()