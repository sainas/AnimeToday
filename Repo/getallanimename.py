# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup


class GetAllAnimeName:

    def __init__(self):
        self.target = 'https://www.crunchyroll.com/videos/anime/alpha?group=all'
        self.server = 'https://www.crunchyroll.com'
        self.title = []
        self.urls = []
        self.nums = []

    def get_url(self):
        req = requests.get(url=self.target)
        html = req.text
        bf = BeautifulSoup(html, "lxml")
        li = bf.find_all('li', itemtype='http://schema.org/TVSeries')
        for each in li[:3]:
            a_bf = BeautifulSoup(str(each), "lxml")
            a = a_bf.find('a')
            print(each.get('group_id'), a.get('title'), self.server + a.get('href'))
        print(len(li))
        # for each2 in div：
        #     print(each2.get('class'))
        #     # a_bf = div_bf[0].find_all('a')


if __name__ == '__main__':
    test = GetAllAnimeName()
    test.get_url()
