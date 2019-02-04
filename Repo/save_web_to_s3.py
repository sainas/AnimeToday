import boto3
import time
import requests

target = 'https://www.crunchyroll.com/videos/anime/alpha?group=all'
req = requests.get(url=target)
html = req.text

s3 = boto3.resource('s3')
date = time.strftime("%Y-%m-%d", time.localtime())
object = s3.Object('animecrawling', date + '/all_anime.txt')
object.put(Body=html)