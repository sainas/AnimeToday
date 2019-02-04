# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    target = 'https://www.crunchyroll.com/videos/anime'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html)
    li = bf.find_all('li', itemtype='http://schema.org/TVSeries')
    div_bf = BeautifulSoup(str(li[15:]))
    div = div_bf.find_all('div', data-classes="container-shadow-dark")
    for each2 in div
        print(each2.get('class'))
        # a_bf = div_bf[0].find_all('a')

    