import threading
import requests
import random

from colorama import Fore

from twocaptcha import TwoCaptcha


api_key = ""
solver = TwoCaptcha(api_key)

cap_url = "https://www.twitch.tv/"
site_key = "E5554D43-23CC-1982-971D-6A2262A2CA24"




readproxy = open('proxies.txt','r')
readproxy2 = readproxy.readlines()
workproxy = []
for proxy3 in readproxy2:
    proxystrip = proxy3.strip('\n')
    workproxy.append(proxystrip)



def Converter():

    proxy1 = random.choice(workproxy)
    proxies = {'http': f'http://{proxy1}','https':f'http://{proxy1}'}

    result = solver.funcaptcha(sitekey='E5554D43-23CC-1982-971D-6A2262A2CA24',url='https://passport.twitch.tv/login',surl='https://twitch-api.arkoselabs.com')
    b = result
    f = b['code'].split('|')[0]
    print(Fore.GREEN + f'\n[+] Generated Captcha Token > {f}')


    content = open('accounts.txt', 'r').read().splitlines()
    url = 'https://passport.twitch.tv/login'

    for user_pass in content:
        username = user_pass.split(':')[0]
        password = user_pass.split(':')[1]

        json = {
            'username': username,
            'password': password,
            'client_id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
            "arkose":{"token":f"{f}|r=eu-west-1|metabgclr=transparent|guitextcolor=%23000000|lang=en-gb|pk=9260643B-49E2-EF5B-2CB5-30FD3451DF51|at=40|sup=1|rid=8|atp=2|cdn_url=https%3A%2F%2Ftwitch-api.arkoselabs.com%2Fcdn%2Ffc|lurl=https%3A%2F%2Faudio-eu-west-1.arkoselabs.com|surl=https%3A%2F%2Ftwitch-api.arkoselabs.com|smurl=https%3A%2F%2Ftwitch-api.arkoselabs.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager",}
        }
        r = requests.post(url, json=json, proxies=proxies)
        if 'access_token' in r.text:
            token = r.json()['access_token']
            print(Fore.GREEN + f"[+] {Fore.RESET}Converted {token}")
            t = open('tokens.txt', 'a')
            t.write(f'{token}\n')

        if 'captcha' in r.text:
            print('Captcha is required..')



def start():
    for i in range(10):
        x = threading.Thread(target=Converter)
        x.start()


start()
