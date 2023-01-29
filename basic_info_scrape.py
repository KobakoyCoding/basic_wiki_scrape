#!/usr/bin/env python3


from bs4 import BeautifulSoup
import random
import requests

user_agents = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Sfari/600.8.9',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
               'Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/108.0.5359.112 Mobile/15E148 Safari/604.1',
               'Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36',
              ]

ua = random.choice(user_agents)
headers = {'User-Agent': ua}


def main():

    page = requests.get('https://en.wikipedia.org/wiki/Chadwick_Boseman', headers={'User-Agent': ua})
    soup = BeautifulSoup(page.text, 'html.parser')
    for item in soup.find_all('td', class_="infobox-data")[0:3]:
        print(item.get_text())


if __name__ == '__main__':
    main()
