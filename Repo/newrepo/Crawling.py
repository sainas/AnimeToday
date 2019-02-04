# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import time
from bostondate import bostondate
import boto3


class Crawling:

    def __init__(self):
        self.target = 'https://www.crunchyroll.com/videos/anime/alpha?group=all'
        self.server = 'https://www.crunchyroll.com'
        self.bucketname = 'animecrawling'
        self.date = bostondate()
        self.s3 = boto3.resource('s3')

    def save_to_s3(self, filename, content):
        object = self.s3.Object(self.bucketname, self.date + '/' + filename )
        object.put(Body=content)

    def get_crawling_list(self):
        req = requests.get(url=self.target)
        all_anime_html = req.text
        soup = BeautifulSoup(all_anime_html, "lxml")
        li = soup.find_all('li', itemtype='http://schema.org/TVSeries')
        self.save_to_s3('all_anime.txt', all_anime_html)
        return li

    def crawl_and_save(self, li):
        anime_url = self.server + li.a.get('href')
        req = requests.get(url=anime_url)
        html = req.text
        self.save_to_s3(li.get('group_id') + '.txt', html)
        print(li.a.get('title'))


if __name__ == '__main__':
    cr = Crawling()
    li = cr.get_crawling_list()
    for each in li:
        cr.crawl_and_save(each)
        time.sleep(1)
